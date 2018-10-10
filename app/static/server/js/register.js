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

var phwrotipli = document.getElementById("ph-form").getElementsByTagName('span');
var emwrotipli = document.getElementById("em-form").getElementsByTagName('span');
var phinput = document.getElementById("ph-form").getElementsByTagName('input');
var eminput = document.getElementById("em-form").getElementsByTagName('input');


document.getElementById("js_DynamicCodePhone").onclick = checkphn;
function checkphn() {
    var js_account_phone = phinput[0].value;
    phwrotipli[0].innerHTML = '';
    var accreg = /^[0-9]{11}/;
    if (js_account_phone.length == 11 && accreg.test(js_account_phone)) {
        requ_dyc('phone',js_account_phone);
    } else {
        phwrotipli[0].innerHTML = '手机号码格式错误^';
    }
}

document.getElementById("js_DynamicCodemail").onclick = checkema;
function checkema() {
    var js_account_mail = eminput[0].value;
    emwrotipli[0].innerHTML = '';
    var emareg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    if (emareg.test(js_account_mail)) {
        requ_dyc('email', js_account_mail);
    } else {
        emwrotipli[0].innerHTML = '邮箱格式错误^';
    }
}


    // document.getElementById("js_submit_reg_phone").onclik = regcheck;
    // document.getElementById("js_submit_reg_mail").onclik = regcheck;


function regcheck(acctype, inv, tipside) {
    // console.log(acctype, inv, tipside)
    if (inv[0].value==''){
        alert('请正确填写表单！')
        return;
    }
    for ( i = 0; i < tipside.length; i++) {
        tipside[i].innerHTML = '';
        
    }
    if(inv[1].value.length>5) {
        if (inv[1].value==inv[2].value){
            if (inv[3].value.length==6){
                ajax_reg(acctype, inv[0].value, inv[1].value, inv[3].value);
            } else { tipside[3].innerHTML = '验证码为六位数^';}
        } else { tipside[2].innerHTML = '密码不一致^';}
    } else { tipside[1].innerHTML = '密码应包含数字、字母、下划线的6 - 18位 ^';}
}


//------AJAX-----



function requ_dyc(keyw, valuew) {
    var xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    } else {
        alert('请用Chrome浏览器访问该页面');
    }
    xmlhttp.open('POST', 'register', true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
    xmlhttp.send(keyw+'='+valuew);
    xmlhttp.onload = function () {
        if (xmlhttp.status == 200) {
            // 如需获得来自服务器的响应，直接使用 XMLHttpRequest 对象的 responseText 或 responseXML 属性。
            interpreter(xmlhttp.responseText);
        }else {
            alert('internet exception');
        }
    }
}

function ajax_reg(acctpye, accnum, pw, dyc) {
    xmlhttp.send(acctpye + '#' + accnum + '#' + pw + '#' + dyc);
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            // 如需获得来自服务器的响应，直接使用 XMLHttpRequest 对象的 responseText 或 responseXML 属性。
            interpreter(xmlhttp.responseText);
        } else {
            alert('internet exception');
        }
    }
}

function interpreter(tipcode) {
    switch (tipcode) {
        case 'accountExist'://账户已存在
            phwrotipli[0].innerHTML ='账户已存在^';
            break;
        case 'numberNotExist'://号码不存在
            phwrotipli[0].innerHTML = '号码不存在^';
            break;
        case 'emailAccountNotExist'://邮箱账号不存在
            phwrotipli[0].innerHTML = '邮箱账号不存在^';
            break;
        case 'done'://完成注册
            // 跳转
            break;
        case 'made':
            phwrotipli[3].innerHTML = '验证码已发送，有效时间3分钟^';
            break;
        case 'breakdyc':
            phwrotipli[3].innerHTML = '验证码错误^';
            break;
        default:
            alert('from distance'+tipcode);
            break;
    }
}