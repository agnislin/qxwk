function submit_course(){
  console.log("add course");
  const request = new XMLHttpRequest();
  request.open("POST", "/admin/course_add");

  c_name = document.querySelector('#input_title').value;
  c_introduction = document.querySelector('#input_info').value;
  c_price = document.querySelector('#input_price').value;
  c_type = document.querySelector('#input_type').value;
  c_lecture = document.querySelector('#input_lecture').value;
  c_date =  document.querySelector('#input_date').value;
 // c_cover =  document.querySelector('#input_logo').value;

  request.onload = () =>{
    const data = request.responseText;
    alert(data)

  };

    // alert(c_name);
  const data = new FormData();
  data.append("name", c_name);
  // alert(c_name);
  data.append("introduction",c_introduction);
  data.append("price", c_price);
  data.append("type",c_type);
  data.append("lecturer",c_lecture);
  data.append("time",c_date);
  // data.append("cover", c_cover)

  request.send(data);
  return false;
};

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


      }
    }
  )
}
