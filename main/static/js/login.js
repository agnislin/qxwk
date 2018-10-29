var wrotip = document.getElementById("wrotip");
var logform = document.getElementById('logform')
function check(){
    wrotip.className = '';
    var account = document.getElementById('account').value;
    var password = document.getElementById('password').value;
    var accreg = /^[0-9]{11}/;
    var emareg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    if (account.length==11 && accreg.test(account)){
        if(password!=''){
            ajax_post()
        } else { wrotip.innerHTML = '请输入密码'; wrotip.className = 'wrophtip';}
    }else if(emareg.test(account)){
        if(password!=''){
            ajax_post()
        } else { wrotip.innerHTML = '请输入密码'; wrotip.className = 'wrophtip';}
    } else {
        wrotip.innerHTML = '请输入正确的手机号或邮箱'; wrotip.className = 'wrophtip';
    }
}

var xmlhttp;
if (window.XMLHttpRequest){
    xmlhttp=new XMLHttpRequest();
}else{alert('请用Chrome浏览器访问该页面')}

xmlhttp.open('POST','login',true);
function ajax_post() {
    xmlhttp.open('POST', 'login', true);
    var formElement = document.getElementById('logform')
    xmlhttp.send(new FormData(formElement))
}
xmlhttp.onload = function(){

    var result = xmlhttp.responseText
    
    if (result == 'redirect') { window.location.href = "http://127.0.0.1:5000/";}
    else { wrotip.className = 'wrophtip';
    wrotip.innerHTML = xmlhttp.responseText;};
    
    xmlhttp.abort();
}