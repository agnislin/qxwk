
//获取登录的账户和密码
function get_login(){
  const request = new XMLHttpRequest();
  request.open("POST","admin/login");
  l_name = document.querySelector('#input_name');
  l_pwd = document.querySelector('#input_pwd');

  request.onload = () =>{
    const data = request.responseText;
    alert(data)

  };

  onst data = new FormData();
  data.append('name',l_name)
  data.append('password',l_pwd)
  request.send(data);
  return false;
};