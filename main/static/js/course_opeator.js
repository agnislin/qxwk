//提交添加课程的信息
function submit_course(){
  console.log("add course");
  const request = new XMLHttpRequest();
  request.open("POST", "/admin/course_add");
  c_teacher = document.querySelector('#input_lecture').value;
  c_name = document.querySelector('#input_title').value;
  c_description = document.querySelector('#input_info').value;
  c_sale = document.querySelector('#input_price').value;
  c_type = document.querySelector('#input_type').value;  
  c_end_time =  document.querySelector('#input_date').value;
 　c_cover =  document.querySelector('#input_logo').value;

  request.onload = () =>{
    const data = request.responseText;
    alert(data)

  };

    // alert(c_name);
  const data = new FormData();
  data.append("teacher", c_teacher);
  // alert(c_name);
  data.append("name",c_name)
  data.append("description",c_description);
  data.append("sale", c_sale);
  data.append("type",c_type);
  data.append("end_time",c_end_time);
  // data.append("cover", c_cover)
  request.send(data);
  return false;
};




//编辑和删除课程
function load_ced(){
  
  document.querySelectorAll('.editCou').forEach(
    button =>{
      button.onclick = () =>{
        const cid = button.dataset.ceid;

      }
    }
  )
  document.querySelectorAll('.removeCou').forEach(
    button =>{
      button.onclick = () =>{
        const cid = button.dataset.cdid;
        const request = new XMLHttpRequest();
        request.open("POST", "/admin/course_del");
        const data = new FormData();
        data.append("cid", cid);
        request.send(data);

        request.onload = () => {
            const data = request.responseText
            if(data=='done'){ document.getElementById(cid).style.display = 'none';
            }else{}
        }

      }
    }
  )
}
