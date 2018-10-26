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


@cms.route('/')
def index():
    return render_template('cms/login.html')


@cms.route('/login',methods = ['GET','POST'])
def login():
    # form = LoginForm()
    if request.method == 'GET':
        return render_template('cms/login.html',)
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        
        # admin = e.AdminInfo(name = "laonanshen",password = "123456")
        # RES = models.find(e.AdminInfo,e.AdminInfo.name == user)
        # print(RES[0].name)
        RES=admin_info = models.find(e.AdminInfo,e.AdminInfo.name==user)
        
        print(user,pwd)
        if user == 'laonanshen' and pwd == '123456':
            return render_template('cms/index.html',user = RES[0])
        else:
            data =[]
            data.append({"error":"用户名或密码有误"})
            print(jsonify(data))
            return jsonify(data)


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



@cms.route('/course_list',methods=['GET','POST'])
def course():     
    rel = models.find(e.Course)
    
    return render_template("cms/course_list.html",rel=rel)

    




# @cms.route('/comment',methods=['GET','POST'])
# def comment(comment_id):
#     if request.method == 'GET':
#         return render_template('/course_list')
#     elif request.method == 'POST':
#         pass


# @cms.log('/log',method=['GET','POST'])
# def log():
#     return render_template('log.html')

@cms.route('/user_list',methods=["GET"])
def show_userlist():
    userl = models.find(e.UserInfo)
    return render_template('cms/user_list.html',userl = userl)




@cms.route('/comment_list',methods=["GET"])
def show_commentlist():
    comml = models.find(e.Comment)
    return render_template('cms/comment_list.html',comml = comml)