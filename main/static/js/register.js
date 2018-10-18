var tabs = document.getElementById("tabs").getElementsByTagName("li");
var ph_form = document.getElementById("ph-form");
var em_form = document.getElementById("em-form");
tabs[0].onclick =show;
tabs[1].onclick =show;

function show(){
    if (tabs[0] === this){
        tabs[0].className = "active";
        tabs[1].className = "";
        ph_form.className = "";
        em_form.className = "non-active";
    }
    else {
        tabs[0].className = "";
        tabs[1].className = "active";
        ph_form.className = "non-active";
        em_form.className = "";
    }
}
//----验证-------
function create() {
    if (window.XMLHttpRequest) {
        return new XMLHttpRequest();
    } else {
        alert('请用Chrome浏览器访问该页面');
    }
}
var xmlhttp = create();

var phinput = document.getElementById("ph-form").getElementsByTagName('input');
var eminput = document.getElementById("em-form").getElementsByTagName('input');

document.getElementById("js_DynamicCodePhone").onclick = checkphn;
function checkphn() {
    var wrotip = document.getElementById('wrophtip');
    var js_account_phone = phinput[0].value;
    wrotip.innerHTML = '';
    var accreg = /^[0-9]{11}/;
    if (js_account_phone.length == 11 && accreg.test(js_account_phone)) {
        requ_dyc('ph');
    } else {
        wrotip.innerHTML = '手机号码格式错误'
        wrotip.className = 'wrophtip';
    }
}


document.getElementById('js_submit_reg_phone').onclick = function () {
    wrotip.innerHTML = '';
    wrotip.className = '';
    var accreg = /^[0-9]{11}/;
    if (phinput[0].length == 11 && accreg.test(phinput[0])){
        if(phinput[1].value.length>5) {
            if (phinput[1].value==phinput[2].value){
                if (phinput[3].value.length==6){
                    regph();
                } else { wrotip.innerHTML = '验证码为六位数';wrotip.className = 'wrophtip';}
            } else { wrotip.innerHTML = '密码不一致';wrotip.className = 'wrophtip';}
        } else { wrotip.innerHTML = '密码应包含数字、字母、下划线的6 - 18位';wrotip.className = 'wrophtip';}
    } else { wrotip.innerHTML = '手机号码格式错误';wrotip.className = 'wrophtip';}
}

document.getElementById("js_submit_reg_mail").onclick = function () {
    var wrotip = document.getElementById('wroemtip');
    var js_account_mail = eminput[0].value;
    wrotip.innerHTML = '';
    wrotip.className = '';
    var emareg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    if (emareg.test(js_account_mail)) {
        if (eminput[1].value.length>5){
            if (eminput[1].value == eminput[2].value){
                regem();
            } else { wrotip.innerHTML = '密码不一致';wrotip.className = 'wrophtip';}
        } else { wrotip.innerHTML = '密码应包含数字、字母、下划线的6 - 18位';wrotip.className = 'wrophtip';}        
    } else {wrotip.innerHTML = '邮箱格式错误';wrotip.className = 'wrophtip';}
}

//------AJAX-----

function requ_dyc() {
    var wrotip = document.getElementById('wrophtip');
    wrotip.innerHTML = '';
    xmlhttp.open('POST', 'register', true);
    var formElement = document.getElementById("ph")
    xmlhttp.send(new FormData(formElement));
    xmlhttp.onload = function () {
            // 如需获得来自服务器的响应，直接使用 XMLHttpRequest 对象的 responseText 或 responseXML 属性。
            wrotip.innerHTML = xmlhttp.responseText
    }
}

function regph() {
    var wrotip = document.getElementById('wrophtip');
    var formElement = document.getElementById("ph")
    xmlhttp.open('POST', 'register', true);
    xmlhttp.send(new FormData(formElement));
    xmlhttp.onload = function () {
        wrotip.innerHTML = xmlhttp.responseText;
        wrotip.className = '';
        wrotip.className = 'wrophtip';
    }
}

function regem() {
    var wrotip = document.getElementById('wroemtip');
    var formElement = document.getElementById("em")
    xmlhttp.open('POST', 'register', true);
    xmlhttp.send(new FormData(formElement));
    xmlhttp.onload = function () {
        wrotip.innerHTML = xmlhttp.responseText;
        wrotip.className = '';
        wrotip.className = 'wrophtip';
    }
}
