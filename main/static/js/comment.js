
document.addEventListener("DOMContentLoaded", () =>{
        loadComment();
        submitCheck("#send-forum", "#forum");
        submitCheck("#send-note", "#note");
    }
);






function getCourseId(){
    return document.querySelector("#vr-base").dataset.vid
};



// 评论框内内容时，禁止提交按钮
function submitCheck(){
    const butt = arguments[0]
    const tarea = arguments[1]
    document.querySelector(butt).disabled = true;
    document.querySelector(tarea).onkeyup = () => {
            if (document.querySelector(tarea).value.length > 0){
                document.querySelector(butt).disabled = false;
            }else{
                document.querySelector(butt).disabled = true;
            }
        };
    };

// 提交评论
document.querySelector('#forum-form').onsubmit = () =>{
    const request = new XMLHttpRequest();
    request.open("POST", "/forum");

    request.onload = () => {
        const data = request.responseText;
        addComment(data);
    };
    const data = new FormData();
    vid = getCourseId()
    comment = document.querySelector("#forum").value
    data.append("content", comment)
    data.append("video_id", vid)
    request.send(data);

    document.querySelector("#forum").value = "";
    document.querySelector('#send-forum').disabled = true;
    return false;
};

// 评论列表滚动事件
document.getElementById('vr-content').onscroll = () => {
    if (document.querySelector("#vr-content").offsetHeight + document.querySelector("#vr-content").scrollTop >= document.querySelector("#vr-content").scrollHeight){
        loadComment();
    };
}

// 加载评论
function loadComment(){
    // 获取记录
    const request = new XMLHttpRequest();
    request.open("POST", "/nextComments");
    request.onload = () => {
        const data = request.responseText;
        addComment(data);
    };
    // 将拉取记录的起始和结束位置 作为请求的参数发送给服务器
    const data = new FormData();
    // data.append('start', start);
    // data.append('end', end);

    // 发送请求
    request.send(data);
};

//  刷新讨论
function addComment(contents){
    document.querySelector('.forum-list').innerHTML = contents + document.querySelector('.forum-list').innerHTML;
};


// document.querySelector("#cour-list").onclick = () =>{
//   const request = new XMLHttpRequest();
//   request.open("Get", "/nextComments");
//   const data = new FormData();
//
//   data.append("course_id", getCourseId());
//   request.send(data);
//
//   request.onload = () => {
//       reslut = request.responseText;
//   };
// };
document.querySelectorAll("[id$=-a]").forEach( panal =>{
    panal.onclick = () => {
        document.querySelectorAll("[id$=-panal]").forEach( p =>{
            p.style.display = "none";
        });

        const panal_name = panal.id.split("-")[0];
        pid = "#"+panal_name+"-panal";
        document.querySelector(pid).style.display = "block";
    }
});

// 隐藏右侧面板
document.querySelector('#hide').onclick = () =>{
    document.querySelector('#v-left').className = "";
    document.querySelector('#v-box').className = "";
    document.querySelector('#show').style.display = "block";
    document.querySelector('#hide').style.display = "none";
};
document.querySelector('#show').onclick = () =>{
    document.querySelector('#v-left').className = "v-left-anim";
    document.querySelector('#v-box').className = "v-box-anim";
    document.querySelector('#hide').style.display = "block";
    document.querySelector('#show').style.display = "none";
};
