




// 设置拉取的位置，第一次为1
let counter = 1;
// 每次拉取的讨论条数
const quantity = 8;


// 评论发送
document.querySelector('#send-forum').disabled = true;
document.querySelector('#text').onkeyup = () => {
    if (document.querySelector('#text').value.length > 0){
        document.querySelector('#send-forum').disabled = false;
    }else{
        document.querySelector('#send-forum').disabled = true;
    }
};
document.querySelector('#forum-form').onsubmit = () =>{
    const request = new XMLHttpRequest();
    request.open("POST", "/forum");

    request.onload = () => {
        const data = JSON.parse(request.responseText);
        data.forEach(add_comment);
        document.querySelector('#text').value = ""
        document.querySelector('#send-forum').disabled = true;
    };

    const data = new FormData();

    request.send(data);

    return false;
};
function add_comment(contents){
    const comm = comm_template({'contents': contents});
    document.querySelector('.forum-list').innerHTML = comm + document.querySelector('.forum-list').innerHTML;
}

// 评论列表滚动事件
document.getElementById('vr-content').onscroll = () => {
    if (document.querySelector("#vr-content").offsetHeight + document.querySelector("#vr-content").scrollTop >= document.querySelector("#vr-content").scrollHeight){
        load();
    };
}
// 当 DOM 加载完成后，进行第一次拉取
document.addEventListener('DOMContentLoaded', load);
function load(){
    // 设置拉取记录所在区间
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    // 获取记录
    const request = new XMLHttpRequest();
    request.open("POST", "/nextComments");

    request.onload = () => {
        const data = request.responseText;
        history_comment(data);
    };
    // 将拉取记录的起始和结束位置 作为请求的参数发送给服务器
    const data = new FormData();
    data.append('start', start);
    data.append('end', end);

    // 发送请求
    request.send(data);
};

// 通过Handlebars模板添加讨论记录到DOM
// const comm_template = Handlebars.compile(document.querySelector('#comment').innerHTML);
function history_comment(contents){
    // 创建新的讨论
    // const comm = comm_template({'contents': contents});
    document.querySelector('.forum-list').innerHTML += contents;
};



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


document.querySelector("#forum-a").onclick = () => {
    document.querySelector("#forum-box").style.display = "block";
    document.querySelector("#note-box").style.display = "none";
    document.querySelector("#coll-box").style.display = "none";
};

document.querySelector("#note-a").onclick = () => {
    document.querySelector("#note-box").style.display = "block";
    document.querySelector("#forum-box").style.display = "none";
    document.querySelector("#coll-box").style.display = "none";
};
document.querySelector("#coll-a").onclick = () => {
    document.querySelector("#coll-box").style.display = "block";
    document.querySelector("#forum-box").style.display = "none";
    document.querySelector("#note-box").style.display = "none";
};
