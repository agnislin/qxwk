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


# @cms.route('/', methods = ['GET','POST'])
# def index():
#     # form = LoginForm()
#     if request.method == 'GET':
#         return render_template('cms/login.html')
#     elif request.method == 'POST':
#         print("index post")
#         user = request.form.get('user')
#         pwd = request.form.get('pwd')

#         admin = e.AdminInfo(name = "laonanshen",password = "123456")
#         RES = models.find(e.AdminInfo,e.AdminInfo.name == user)
#         print(RES)
#         # print(RES[0].name)
#         # return jsonify({"data": 123})o = models.find(e.AdminInfo,e.AdminInfo.name==user)

#         print(user,pwd)
#         if user == 'laonanshen' and pwd == '123456':
#             return  render_template('cms/index.html',user = RES)
#         else:
#             # data =[]
#             # data.append({"error":"用户名或密码有误"})
#             # print(jsonify(data))# return jsonify({"data": 123})

#             return render_template('cms/login.html')

@cms.route('/')
def index():
    name=session.get('aid', False)
    if name:
        return render_template('cms/index.html', user=name)
    else:
        return redirect(url_for('cms.login'))

#登录
@cms.route('/login',methods = ['GET','POST'])
def login():

    if request.method == "GET":
        return render_template('cms/login.html')
    else:   
        name = request.form.get('user')
        password = request.form.get('pwd')
        admin = e.AdminInfo.query.filter(e.AdminInfo.name == name).first()
        if admin and admin.password == password:
            session['aid'] = name
            # return redirect(url_for('cms.index'))
            return render_template('cms/index.html',admin_profile = admin.profile,admin_name = admin.name)
        else:
            return render_template('cms/login.html',error="用户名或密码有误！")

@cms.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('cms.index'))



# @cms.route('/user')
# def show_username(username):
#     user_id = request.args.get('delete')
#     if user_id is not None:
#         return username

#     user = request.args.get('username')
#     course = request.args.get('courseId')
#     if not (user and course):
#         return user + course


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
        # id = request.form['id']
        teacher = request.form['teacher']
        name = request.form['name']
        description = request.form['description']
        sale = request.form['sale']
        leix = request.form['type']       
        end_time = request.form['end_time']
        f = request.files['cover']
        f1 = request.files['video']
        print(f)
        print(f1)
    except:
        return 'ererer'
    else:
        course = e.Course(teacher = teacher,name =name,description = description,
            sale = sale,type = leix,end_time = end_time)
        print(f1)
        try:
            f.save('main/static/jpg/'+f.filename)
        except Exception as m:
            print(m)


        try:
            f1.save('static'+f1.filename)
        except Exception as o:
            print(o)
     
        res = models.save(course)
        
        if res == True:
            return "添加课程成功！"
        elif res == False:
            return "添加课程失败！"

        # return jsonify({"data": 123})


#编辑课程
@cms.route('/course_edit',methods=["GET","POST"])
def course_edit():
    if request.method == "GET":
        id = request.args.get('id','')
        course = models.Course.query.filter(models.Course.id == course_id).first()
        return render_template('/course_list.html',course = course)
    elif request.method == "POST":
        try:
            id = request.form['id']
            teacher = request.form['teacher']
            name = request.form['name']
            description = request.form['description']
            sale = request.form['sale']
            leix = request.form['type']       
            end_time = request.form['end_time']
            f = request.files['cover']
            f1 = request.files['video']
        except:
            return "error"
        else:
            course = e.Course(teacher = teacher,name =name,description = description,
            sale = sale,type = leix,end_time = end_time)
        try:
            f.save('main/static/jpg/'+f.filename)
        except Exception as m:
            print(m)
        try:
            f1.save('static'+f1.filename)
        except Exception as o:
            print(o)
        res = models.save(course)
        
        if res == True:
            return "修改课程成功！"
        elif res == False:
            return "修改课程失败！"



#删除课程
@cms.route('/course_del',methods=['POST'])
def course_del():
    course_id = request.form['cid']
    # res = models.remove(e.Course,e.Course(id=course_id))
    course = models.Course.query.filter(models.Course.id == course_id).first()
    models.db.session.delete(course)
    try:
        res = models.db.session.commit()
        print(res)
    except Exception as e:
        print(e)
    if res == None:
        return "done"
    else:
        return "fail"




#会员（用户）列表
@cms.route('/user_list',methods=["GET"])
def show_userlist():
    userl = models.find(e.UserInfo)
    return render_template('cms/user_list.html',userl = userl)



#删除会员（用户）
@cms.route('/user_del',methods=['POST'])
def user_del():
    user_id = request.form['uid']
    user = models.UserInfo.query.filter(models.UserInfo.id == user_id).first()
    models.db.session.delete(user)
    try:
        res = models.db.session.commit()
       
    except Exception as e:
        print(e)
    if res == None:
        return "done"
    else:
        return "fail"


#评论列表
@cms.route('/comment_list',methods=["GET"])
def show_commentlist():
    comml = models.find(e.Comment)
    return render_template('cms/comment_list.html',comml = comml)



#删除评论
@cms.route('/comment_del',methods = ["POST"])
def comment_del():
    comment_id = request.form['cmid']
    comment = models.Comment.query.filter(models.Comment.id == comment_id).first()
    models.db.session.delete(comment)
    try:
        res = models.db.session.commit()
    except Exception as e:
        print(e)
    if res == None:
        return "done"
    else:
        return "fail"

#会员登录日志列表
@cms.route('/userloginlog_list',methods = ["GET"])
def show_userloginloglist():
    userlogl = models.find(e.Learning_log)
    print(userlogl)
    return render_template('cms/userloginlog_list.html',userlogl = userlogl)


#操作日志
@cms.route('/oplog_list',methods = ['GET'])
def show_oploglist():
    oplogl = models.find(e.OperationLog)
    print(oplogl)
    return render_template('cms/oplog_list.html',oplogl = oplogl)


#管理员列表
@cms.route('/admin_list',methods=["GET"])
def show_adminlist():
    adminl = models.find(e.AdminInfo)    
    return render_template('cms/admin_list.html',adminl = adminl)


#添加管理员
@cms.route('/admin_add',methods=['POST'])
def admin_add():
    try:
        name = request.form['name']
        password = request.form['password']
        super_power = request.form['super_power']
        print(super_power)                
    except:
        return 'error'
    else:
        admin = e.AdminInfo(name = name,password = password,super_power = int(super_power)
            )
        res = models.save(admin)
        print(res)
        if res == True:
            return "添加管理员成功！"
        elif res == False:
            return "添加管理员失败！"


