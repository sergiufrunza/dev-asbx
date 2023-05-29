

let copyright = document.getElementById("copyright-txt");
const current = new Date;
copyright.innerHTML +=`Copyright © ${current.getFullYear()} ASBX.ORG All Rights Reserved`
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
    el:'#calculatorPage',
    data:{
        listStates:[],
        listDiseases:[],
        listIndustries:[],
        jobs: {},
        jobGroups:[],
        zipcode:'',
        aboutAnything:false,
        activeStep: 1,
        phoneLookup:'',
        currentWorkState:{},
        currentJobIndutries:[],
        WorkInState:false,
        workStateList:[],
        currentJobGroups:[],
        Client:{
            aboutAnything:'',
            yearForDeath:'',
            SOLDate:{
                current:'',
                recently:'',
                before:'',
                },

            yearTo:'',
            workBeforeYear:'',
            victim:'',
            lives:'',
            jobs:[],
            disease:'',
            phoneValidFormat:false,
            smoker:'',
            phone:'',
            code:'',
            checkCode:false,
            resident_state: {},
            work_states:[],
            yearForDiagnosed:"",
            city:'',
        },
    },
    methods: {
        addWorkState: function (){
            const obj = this;
            obj.currentWorkState=obj.Client.resident_state;
        },
        deleteWorkState: function (){
            const obj = this;
            obj.currentWorkState= {};
        },
        goToStep: async function (index){
            const obj = this;
            switch (index){
                case 1:
                    location.reload();
                    break;
                case 2:
                    await axios.get('api/v1/statelist/')
                        .then(function (response){
                            obj.listStates = response.data
                });
                    await axios.get('https://ipapi.co/json/')
                        .then(function (response) {
                            var name
                            if(response.data["region"] === "District of Columbia"){
                              name = "Washington, D.C."
                            }
                            else{
                                name = response.data["region"]
                            }
                            obj.zipcode = response.data["postal"];
                            obj.Client.resident_state = {
                                "abbr":response.data["region_code"],
                                "name":name
                            };
                            obj.Client.city = response.data["city"]
                        });
                    break;

                case 3:
                    await axios.get('api/v1/diseaseslist/')
                        .then(function (response){
                            obj.listDiseases = response.data
                })
                    break;

               case 15:
                    obj.Client.work_states.push(
                        {
                            "name":obj.currentWorkState.name,
                            "abbr":obj.currentWorkState.abbr,
                            "industry":obj.currentJobIndutries,
                            "jobgroup":obj.currentJobGroups,
                        }
                    )
                    obj.currentJobIndutries=[]
                    obj.currentJobGroups=[]
                    obj.currentWorkState={};
                   break;

                case 7:
                    await axios.post('api/v1/jobsindustrylist/',{
                        header: {
                            "X-CSRFToken": CSRF_TOKEN,
                        },
                        "state": obj.currentWorkState.abbr,
                    })
                        .then(function (response) {
                           obj.listIndustries = response.data
                        })
                    obj.WorkInState=false;
                    break;

                case 8:
                    await axios.post('api/v1/yearwork/',{
                        header: {
                            "X-CSRFToken": CSRF_TOKEN,
                        },
                        "work_state": obj.Client.work_states,
                    })
                        .then(function (response) {
                           obj.Client.yearTo = response.data["year"]
                        })
                    break;
                case 9:
                    await axios.post('api/v1/stateoflimitation/', {
                        header: {
                            "X-CSRFToken": CSRF_TOKEN,
                        },
                        "resident_state": obj.Client.resident_state.abbr
                    })
                        .then(function (response) {
                            const current = new Date;
                            obj.Client.SOLDate.current=`${current.getFullYear()}`;
                            obj.Client.SOLDate.recently=`${current.getFullYear() - 1} - ${current.getFullYear() - response.data["year_death"]}`;
                            obj.Client.SOLDate.before=`Before ${current.getFullYear() - response.data["year_death"]}`;
                        });
                    break;
                    case 16:
                    await axios.post('api/v1/stateoflimitation/', {
                        header: {
                            "X-CSRFToken": CSRF_TOKEN,
                        },
                        "resident_state": obj.Client.resident_state.abbr
                    })
                        .then(function (response) {
                            const current = new Date;
                            obj.Client.SOLDate.current=`${current.getFullYear()}`;
                            obj.Client.SOLDate.recently=`${current.getFullYear() - 1} - ${current.getFullYear() - response.data["year_diagnosed"]}`;
                            obj.Client.SOLDate.before=`Before ${current.getFullYear() - response.data["year_diagnosed"]}`;
                        });
                    break;

                case 12:
                     await axios.post('api/v1/sendverificationcode/', {
                        header: {
                            "X-CSRFToken": CSRF_TOKEN,
                        },
                        "phone": obj.Client.phone
                    })
                        .then(function () {
                        });
                    break;

                case 13:
                    await axios.post('api/v1/getjobgrupslist/', {
                        header: {
                            "X-CSRFToken": CSRF_TOKEN,
                        },
                        "industry": obj.currentJobIndutries
                    })
                        .then(function (response) {
                            obj.jobGroups = response.data
                        });
                    break;
            }
            obj.activeStep=index;
        },
        validatePhoneNumber: function () {
            const obj = this;
            const DEFAULT_COUNTRY = 'US'
            const formatter = new libphonenumber.AsYouType(DEFAULT_COUNTRY)
            formatter.reset()
            const newValue = formatter.input(obj.Client.phone)
            if(newValue[newValue.length-1] !== ")")
                obj.Client.phone = newValue
            if (libphonenumber.isValidPhoneNumber(newValue, DEFAULT_COUNTRY)) {
                obj.Client.phoneValidFormat = true;
                if (newValue[0]==="1"){
                    obj.Client.phone = "+"+ newValue
                }
                else if(newValue[0]==="+"){
                    obj.Client.phone = newValue
                }
                else{
                    obj.Client.phone = "+1 "+newValue
                }
            }
            else{
                obj.Client.phoneValidFormat = false;
            }
            //end validatePhoneNumber
        },
        goToResultPage: async function () {
            const obj = this
            await axios.post('api/v1/createclient/', {
                header: {
                    "X-CSRFToken": CSRF_TOKEN,
                },
                "disease": obj.Client.disease,
                "victim": obj.Client.victim,
                "lives": obj.Client.lives,
                "additional_info": obj.Client.aboutAnything,
                "phone": obj.Client.phone,
                "resident_state": obj.Client.resident_state.abbr,
                "work_states": obj.Client.work_states,
                "smoker": obj.Client.smoker,
                "deceased":obj.Client.yearForDeath,
                "diagnosed":obj.Client.yearForDiagnosed,


            })
                .then( async function (response) {
                    if (response.data.status) {
                        localStorage.setItem("ClientToken", response.data.token)
                        localStorage.setItem("WorkHistory", JSON.stringify(obj.Client.work_states))
                        localStorage.setItem("ClientExist","0")
                        window.location.href = "/result"
                    }
                });
        },

        checkCode : async  function (){
            const obj = this
            if (obj.Client.code.length == 4){
              await axios.post('/api/v1/checkverificationcode/', {
                        header: {
                            "X-CSRFToken": CSRF_TOKEN,
                        },
                        "code": obj.Client.code,
                        "phone": obj.Client.phone,
                    })
                        .then(function (response) {
                            if (response.data.status){
                                obj.goToResultPage();
                            }

                        });
            }
            //end checkCode
        },

    //end methods
    },
    //end class Vue
});



