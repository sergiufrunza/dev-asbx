
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

// var CSRF_TOKEN=getCookie('csrftoken');
// axios.defaults.xsrfHeaderName = "X-CSRFToken";
