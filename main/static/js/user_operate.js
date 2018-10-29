//删除用户
function load_remu(){
  
    document.querySelectorAll('.removeUser').forEach(
        
        button =>{
            button.onclick = () =>{
                const uid = button.dataset.udid;
                const request = new XMLHttpRequest();
                request.open("POST","/admin/user_del")
                const data = new FormData();
                data.append("uid",uid)
                request.send(data); 

                request.onload = () => {
                    const data = request.responseText
                    if(data=='done'){ document.getElementById(uid).style.display = 'none';
                    }else{}
                }

            }
            
        }
    )

}