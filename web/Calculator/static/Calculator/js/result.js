
let copyright = document.getElementById("copyright-txt");
const current = new Date;
copyright.innerHTML +=`Copyright © ${current.getFullYear()} ASBX.ORG All Rights Reserved`;
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var CSRF_TOKEN=getCookie('csrftoken');
axios.defaults.xsrfHeaderName = "X-CSRFToken";


new Vue({
    el:'#resultPage',
    data:{
        activePopupEr:false,
        activePopupAvg:false,
        activePopupIr:false,
        FullName:"",
        Email:"",
        currentData:"",
        ClientToken:"",
        ResultClient:{},
        ClientExist:false,
        validEmail:false,
        },
    methods: {
        sendEmailDocuSign: async function () {

            const obj = this;
            obj.validEmail=false
            obj.activePopupEr=false
            obj.activePopupAvg=false
            obj.activePopupIr=false
            await axios.post('/api/v1/sendemaildocusign/', {
                header: {
                    "X-CSRFToken": CSRF_TOKEN,
                    "Token": obj.ClientToken,
                },
                "compensation": obj.ResultClient.compensation,
                "disease": obj.ResultClient.disease,
                "phone": obj.ResultClient.phone,
                "state": obj.ResultClient.state,
                "full_name":obj.FullName,
                "email_address":obj.Email,

            })
                .then(function () {

                });
        },



        sendEmail: async function () {
            const obj = this;
            obj.WorkHistory = JSON.parse(localStorage.getItem("WorkHistory"))
            await axios.post('/api/v1/sendemail/', {
                header: {
                    "X-CSRFToken": CSRF_TOKEN,
                    "Token": obj.ClientToken,
                },
                "work_states": obj.WorkHistory,
                "compensation": obj.ResultClient.compensation,
                "disease": obj.ResultClient.disease,
                "victim": obj.ResultClient.victim,
                "smoker": obj.ResultClient.smoker,
                "phone": obj.ResultClient.phone,
                "about": obj.ResultClient.about,
                "state": obj.ResultClient.state,
                "deceased":obj.ResultClient.deceased,
                "diagnosed":obj.ResultClient.diagnosed,
                "lives":obj.ResultClient.lives,

            })
                .then(function () {
                    localStorage.setItem("ClientExist", "1")
                });
        },
        getClientResult: async function () {
            const obj = this;
                await axios.get('/api/v1/getclientinfo/', {
                    headers: {
                        "Token": obj.ClientToken,
                        "X-CSRFToken": CSRF_TOKEN,
                    },
                }).then(function (response) {
                    obj.ResultClient = response.data
                    obj.ClientExist = true;
                    if (!(localStorage.getItem("ClientExist")==="1")) {
                        obj.sendEmail();
                    }
                });

        },

        validateEmail:function (){
        const obj = this;
        let inputform = document.getElementById("email-input-form");
        var pattern = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        if(obj.Email.match(pattern)){
            inputform.style.borderColor = "#11845b";
            obj.validEmail=true;
        }
        else{
            inputform.style.borderColor = "#b40003";
            obj.validEmail=false;
        }
    }
    //end methods
    },
    mounted:function () {
        const obj = this;
        if (localStorage.getItem("ClientToken")) {
            obj.ClientToken = localStorage.getItem("ClientToken")
            obj.getClientResult()
            const month = ["January","February","March","April","May","June","July","August","September","October","November","December"];
            const current = new Date;
            obj.currentData= `${month[current.getMonth()]} ${current.getDate()}, ${current.getFullYear()}`
        }
    },
    //end class Vue
});