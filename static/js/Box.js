/**
 * Created by symenyang on 2017/5/15.
 */



var box = new Vue({
    el:"#point-shower",
    data:{
        show : false,
        title : "",
        status : "",
        percent : "",
        type : 0,
        ID : 0,
        introduction : "",
        problems : [],
        practice : "",
        userAns : [],
        canLearn : "0",
        showProblem : false,
        links : []
    },
    methods:{
        showBox:function (d) {
            this.title = d.name;
            this.percent = d.proc;
            this.type = d.type;
            if (nameBox.userName == "Login")
                this.type = 1;
            this.ID = d.ID;
            this.problems = [];
            this.showProblem = false;
            this.userAns = [];

           if (this.percent === 0)
               if (this.type == 0)
                   this.status = "待学";
                else
                    if (nameBox.userName == "Login")
                        this.status = "请登陆";
                    else
                        this.status = "目标";
           else
               this.status = "已完成";
           this.show = true;



           axios.post('/api/getPointInfo',{
                ID : d.ID
           })
           .then(function (response) {
               box.introduction = response.data;
           })
           .catch(function (error) {
               console.log(error);
           });

           axios.post('/api/getLinks',{
                ID : d.ID
           })
           .then(function (response) {
               box.links = response.data;
           })
           .catch(function (error) {
               console.log(error);
           });

           if (nameBox.userName == "Login")
               return;

            axios.post('/api/getCanLearn',{
                ID : d.ID
            }).then(function (response) {
                box.canLearn = response.data;
                if (box.canLearn == "1"){
                    box.practice = "请先完成前置知识点";
                }
                else{
                    box.getProblems();
                    box.showProblem = true;
                }
            }).catch(function (error) {
               console.log(error);
            });


        },
        getProblems:function () {
            axios.post('/api/getProblems',{
               ID : this.ID
           })
           .then(function (response) {
               box.problems = response.data;
               if (box.problems.length != 0)
                   box.practice = "开始练习吧";

               else
                   box.practice = "";
           })
           .catch(function (error) {
               console.log(error);
           });
        },
        unshowBox:function (event) {
            this.show = false;
            svg.attr("transform", "translate(" + -offsetx + "," + -offsety + ")scale(1)");
            svgmove.translate([-offsetx,-offsety]);
        },
        setAsTarget:function (event) {
            axios.post('/api/setTarget',{
                ID: this.ID
            }).then(function (response) {
                clean();
                box.type = 1;
                addData(nameBox.userName);
            }).catch(function (error) {
               console.log(error);
           });
        },
        submit:function (event) {
            var l = this.problems.length;
            var cor = 0;
            for (var i = 0;i < l;++i)
            {
                if (parseInt(this.userAns[i]) == this.problems[i].answer)
                    cor ++;
            }
            var score = (100 * cor) / l;

            axios.post('/api/submitScore',{
                ID : this.ID,
                score : score
            }).then(function (response) {

            }).catch(function (error) {
               console.log(error);
            });
            this.unshowBox();
            clean();
            addData(nameBox.userName);
        }
    }
});