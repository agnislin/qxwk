document.querySelector('#add_course_form').onsubmit = () => {

  console.log("add course")
  const request = new XMLHttpRequest();
  request.open("POST", "/admin/course_add");

  c_name = document.querySelector('#input_title').value;
  c_introduction = document.querySelector('#input_info').value
  c_price = document.querySelector('#input_price').value
  c_type = document.querySelector('#input_type').value
  c_lecture = document.querySelector('#input_lecture').value
  c_date = = document.querySelector('#input_date').value


  // alert(c_name);
  const data = new FormData();
  data.append("name", c_name);
  // alert(c_name);
  data.append("introduction",c_introduction)
  data.append("price", c_price);
  data.append("type",c_type)
  data.append("lecturer",c_lecture)
  data.append("date",c_date)

  request.send(data)
  return false;
};
