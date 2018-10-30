


function changeHtml(htm){
    document.querySelector('.content-wrapper').innerHTML = htm;
};


function reurl(url){
    const request = new XMLHttpRequest()
    request.open("POST", "/admin/reurl")

    request.onload = () => {
        const data = request.responseText;
        console.log(data);
        changeHtml(data);
    };

    const data = new FormData();
    data.append('page', url);

    request.send(data);
    return false;

};

//课程列表
function courselist(contents){
    const comm = comm_template({'contents': contents});
    document.querySelector('.forum-list').innerHTML = comm + document.querySelector('.forum-list').innerHTML;
}




function course_list(url){
    const request = new XMLHttpRequest()
    request.open("GET", "/admin/course_list")

    request.onload = () => {
        const data = request.responseText;
        console.log(data);
        changeHtml(data);
        load_ced();
        // submit_course();
    };

    const data = new FormData();
    data.append('page', url);

    request.send(data);
    return false;

};


function user_list(url){
    const request = new XMLHttpRequest()
    request.open("GET", "/admin/user_list")

    request.onload = () => {
        const data = request.responseText;
        console.log(data);

        changeHtml(data);
        load_remu();//加载页面
    };

    const data = new FormData();
    data.append('page', url);

    request.send(data);s
    return false;

};

function comment_list(url){
    const request = new XMLHttpRequest()
    request.open("GET", "/admin/comment_list")

    request.onload = () => {
        const data = request.responseText;
        console.log(data);
        changeHtml(data);
        load_remco()
        
    };

    const data = new FormData();
    data.append('page', url);

    request.send(data);
    return false;

};

function userloginlog_list(url){
        const request = new XMLHttpRequest()
        request.open("GET", "/admin/userloginlog_list")

        request.onload = () => {
            const data = request.responseText;
            console.log(data);
            changeHtml(data);
            
        };

        const data = new FormData();
        data.append('page', url);

        request.send(data);
        return false;

    };


function oplog_list(url){
        const request = new XMLHttpRequest()
        request.open("GET", "/admin/oplog_list")

        request.onload = () => {
            const data = request.responseText;
            console.log(data);
            changeHtml(data);
            
        };

        const data = new FormData();
        data.append('page', url);

        request.send(data);
        return false;

    };

function admin_list(url){
    const request = new XMLHttpRequest()
    request.open("GET", "/admin/admin_list")

    request.onload = () => {
        const data = request.responseText;
        console.log(data);
        changeHtml(data);
        // submit_admin();
    };

    const data = new FormData();
    data.append('page', url);

    request.send(data);
    return false;

};


