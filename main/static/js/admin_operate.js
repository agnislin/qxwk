//提交添加管理员的信息
function submit_admin(){
    const request = new XMLHttpRequest();
    request.open("POST", "/admin/admin_add");

    a_name = document.querySelector('#input_name').value;
    a_pwd = document.querySelector('#input_pwd').value;
    a_super_power = document.querySelector('#input_type').value;
    if (a_super_power == "超级管理员")
        {num = 1;}
    else 
        {num = 0;}

    

    request.onload = () =>{
        const data = request.responseText;
        alert(data)

    };
    const data = new FormData();
    data.append('name',a_name);
    data.append('password',a_pwd);
    data.append('super_power',num);   

    request.send(data)
    return false;
};