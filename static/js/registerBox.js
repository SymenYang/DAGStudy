/**
 * Created by symenyang on 2017/5/21.
 */
var registerBox = new Vue({
    el : "#register-box",
    data : {
        show : false,
        error : "",
        userName :"",
        password:"",
        repassword:""
    },
    methods : {
        unshowBox:function (event) {
            this.show = false;
            svg.attr("transform", "translate(" + -offsetx + "," + -offsety + ")scale(1)");
            svgmove.translate([-offsetx,-offsety]);
        },
        showBox:function () {
            this.userName = "";
            this.password = "";
            this.repassword = "";
            this.error = "";
            this.show = true;
        },
        submit: function() {
            if(this.repassword != this.password) {
                this.error = "Password not equal";
                this.password = "";
                this.repassword = "";
                return;
            }
            axios.post('/api/register',{
                username : this.userName,
                password : this.password
            })
                .then(function (responce) {
                    console.log(responce.data);
                    if (responce.data == 0){
                        nameBox.userName = registerBox.userName;
                        clean();
                        addData(registerBox.userName);
                        registerBox.unshowBox();
                    }
                    if (responce.data == 1){
                        registerBox.error = "User already exist";
                        registerBox.userName = "";
                        registerBox.password = "";
                        registerBox.repassword = "";
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    }
});