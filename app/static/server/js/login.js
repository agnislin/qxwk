var wroac = document.getElementById("wro-ac");
var wropw = document.getElementById("wro-pw");
function check(){
    var account = document.getElementById('account').value;
    var password = document.getElementById('password').value;

    wroac.innerHTML='';
    wropw.innerHTML='';
    var accreg = /^[0-9]{11}/;
    var emareg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    if (account.length==11 && accreg.test(account)){
        // alert(accreg.test(account));
        // console.log(accreg.test(account));
        if(password!=''){
            ajax_post(account, password)
        }else{wropw.innerHTML='请输入密码';}
    }else if(emareg.test(account)){
        if(password!=''){
            ajax_post(account, password)
        }else{wropw.innerHTML='请输入密码';}
    } else {
    wroac.innerHTML ='请输入正确的手机号或邮箱';
    }
}


var xmlhttp;
if (window.XMLHttpRequest){
    // 创建XMLHttpRequest对象
    xmlhttp=new XMLHttpRequest();
}else{
    alert('请用Chrome浏览器访问该页面')
}
// open(method, url, async)方法规定请求的类型、URL 以及是否异步处理请求。
xmlhttp.open('POST','login',true);
// 如果需要像 HTML 表单那样 POST 数据，请使用 setRequestHeader() 来添加 HTTP 头。
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
function ajax_post(account, password) {
    s = 'account='+account+'&password='+password;
    // send() 方法发送数据
    xmlhttp.send(s)
}
xmlhttp.onreadystatechange = function(){
    if (xmlhttp.readyState==4 && xmlhttp.status==200){
        // 如需获得来自服务器的响应，直接使用 XMLHttpRequest 对象的 responseText 或 responseXML 属性。
        alert(xmlhttp.responseText);
        var tip = xmlhttp.responseText;
        if(tip=='wrong-ac'){
            wroac.innerHTML = '账号不存在';//账号不存在
        }else if(tip=='wrong-pw'){
            wropw.innerHTML = '密码错误';//密码错误
        }else if(tip==OK){
            // 跳转到首页
            // wroac.innerHTML = '<p "style="color:green;font-size:18px;margin-left:60px;"">成功，即将跳转</p>';
            return true;
        }

    }
}