/**
 * Created by symenyang on 2017/5/21.
 */
var loginBox = new Vue({
    el : "#login-box",
    data : {
        show : false,
        error : "",
        userName :"",
        password:""
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
            this.error = "";
            this.show = true;
        },
        submit: function() {
            axios.post('/api/login',{
                username : this.userName,
                password : this.password
            })
                .then(function(response){
                    if(response.data == 0)
                    {
                        nameBox.userName = loginBox.userName;
                        clean();
                        addData(loginBox.userName);
                        loginBox.unshowBox();
                    }
                    if (response.data == 1)
                    {
                        loginBox.userName = "";
                        loginBox.password = "";
                        loginBox.error = "No such user";
                    }
                    if (response.data == 2)
                    {
                        loginBox.password = "";
                        loginBox.error = "Password Error";
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
        register: function () {
            console.log("here");
            this.unshowBox();
            registerBox.showBox();
        }
    }
});