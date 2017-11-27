/**
 * Created by symenyang on 2017/5/16.
 */

var nameBox = new Vue({
    el : "#name-shower",
    data : {
        userName : ""
    },
    created:function () {
        axios.get('/api/getName')
            .then(function (responce) {
                nameBox.userName = responce.data;
                if (nameBox.userName != "Login"){
                        clean();
                        addData(nameBox.userName);
                }
            })
    },
    methods : {
        restart : function (event) {
            var p = force.nodes();
            p[0].fixed = true;
            p[0].x = width / 2;
            p[0].y = height / 2;
            p[0].px = width / 2;
            p[0].py = height / 2;
            var l = p.length;
            for (var i = 1;i < l; ++i)
            {
                p[i].fixed = false;
                p[i].x = width / 2 + Math.random() * 200;
                p[i].y = height / 2 + Math.random() * 200;
            }
            svg.attr("transform", "translate(" + -offsetx + "," + -offsety + ")scale(1)");
            svgmove.translate([-offsetx,-offsety]);
            force.alpha(0.5).start();
        },
        toggleLog : function (event) {
            if (this.userName == "Login")
            {
                loginBox.showBox();
                console.log("login");
            }
            else
            {
                console.log("logout");
                axios.get('/api/logout');
                clean();
                addData("Login");
                this.userName = "Login";
            }
        }
    }
});