//删除评论
function load_remco(){
  
    document.querySelectorAll('.removeComment').forEach(
        
        button =>{
            button.onclick = () =>{
                const cmid = button.dataset.cmdid;
                const request = new XMLHttpRequest();
                request.open("POST","/admin/comment_del")
                const data = new FormData();
                data.append("cmid",cmid)
                request.send(data); 

                request.onload = () => {
                    const data = request.responseText
                    if(data=='done'){ document.getElementById(cmid).style.display = 'none';
                    }else{}
                }

            }
            
        }
    )

}