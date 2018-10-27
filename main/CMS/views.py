# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import cms
import models
import entry as e
from flask import Flask, jsonify, render_template, request,redirect,url_for,flash,session
from functools import wraps


# #限制访问控制
# def admin_login_req(f):
#     @wraps(f)
#     def decorated_function(*args,**kwargs):
#         if not session.has_key("admin"):
#             return redirect(url_for("cms/login.html",next=request.url))
#         return f(*args,**kwargs)
#     return decorated_function


@cms.route('/', methods = ['GET','POST'])
def index():
    # form = LoginForm()
    if request.method == 'GET':
        return render_template('cms/login.html')
    elif request.method == 'POST':
        print("index post")
        user = request.form.get('user')
        pwd = request.form.get('pwd')

        admin = e.AdminInfo(name = "laonanshen",password = "123456")
        RES = models.find(e.AdminInfo,e.AdminInfo.name == user)
        # print(RES[0].name)
        # return jsonify({"data": 123})o = models.find(e.AdminInfo,e.AdminInfo.name==user)

        print(user,pwd)
        if user == 'laonanshen' and pwd == '123456':
            return  render_template('cms/index.html',user = RES[0])
        else:
            data =[]
            data.append({"error":"用户名或密码有误"})
            print(jsonify(data))# return jsonify({"data": 123})
            return jsonify(data)



#登录
# @cms.route('/login',methods = ['GET','POST'])
# def login():
#
# return render_template('cms/login.html')


# return jsonify({"data": 123})



@cms.route('/user')
def show_username(username):
    user_id = request.args.get('delete')
    if user_id is not None:
        return username

    user = request.args.get('username')
    course = request.args.get('courseId')
    if not (user and course):
        return user + course


@cms.route('/reurl',methods=['GET','POST'])
def reurl():
    print("resul")
    if request.method == 'POST':
        path = request.form['page']
        print(path)
        return render_template("cms/%s.html" % path)


#
# @cms.route('/delete', methods=['POST'])
# def cou_delete():
#     if request.method == 'POST':
#         print(request.form['cou_id'])
#         return 'dd'


#课程列表
@cms.route('/course_list',methods=['GET','POST'])
def course():
    rel = models.find(e.Course)
    return render_template("cms/course_list.html",rel=rel)





#添加课程
@cms.route('/course_add',methods=['POST'])
def course_add():
    try:
        print(request.form)
        name = request.form['name']
        introduction = request.form['introduction']
        type = request.form['type']
        price = request.form['price']
        lecturer = request.form['lecturer']
        time = request.form['time']
        # cover = request.form['cover']
    except:
        return 'ererer'
    else:
        course = e.Course(course=name,introduction=introduction,type=type,cost=price,
        lecturer=lecturer,date=time)


    res = models.save(course)
    if res == True:
        return "添加课程成功！"
    elif res == False:
        return "添加课程失败！"

    # return jsonify({"data": 123})


#删除课程
@cms.route('/course_add',methods=['GET','POST'])
def course_del():
    course_id = request.form['id']
    res = models.remove(e.Course,e.Course(id=course_id))
    if res == True:
        return "删除课程成功！"
    elif res == False:
        return "删除课程失败！"
#
# @cms.route('/delete/<cou_id>')
# def delete(cou_id):
#     res = models.remove(e.Course,e.Course(id=cou_id))
#     if res == True:
#         return render_template('cms/course_list.html')
#     elif res == False:
#         return "删除课程失败！"


# @cms.route('/comment',methods=['GET','POST'])
# def comment(comment_id):
#     if request.method == 'GET':
#         return render_template('/course_list')
#     elif request.method == 'POST':
#         pass


# @cms.log('/log',method=['GET','POST'])
# def log():
#     return render_template('log.html')


#会员（用户）列表
@cms.route('/user_list',methods=["GET"])
def show_userlist():
    userl = models.find(e.UserInfo)
    return render_template('cms/user_list.html',userl = userl)



#评论列表
@cms.route('/comment_list',methods=["GET"])
def show_commentlist():
    comml = models.find(e.Comment)
    return render_template('cms/comment_list.html',comml = comml)




#管理员列表
@cms.route('/admin_list',methods=["GET"])
def show_adminlist():
    admin = models.find(e. AdminInfo)
    return render_template('cms/admin_list.html',admin = admin)

#添加管理员
@cms.route('/admin_add',methods=['POST'])
def admin_add():
    name = request.form['name']
    passward = request.form['password']
    date = request.form['date']
    picture = request/form['picture']
    admin = e.AdminInfo(name = name,password = password,date = date,picture = picture)
    models.save(admin)
    return "添加课程成功！"
