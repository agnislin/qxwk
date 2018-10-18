# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import render_template, request
from . import cms


@cms.route('/')
def index():
    return render_template('cms/index.html')


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





@cms.route('/comment',methods=['GET','POST'])
def comment(comment_id):
    if request.method == 'GET':
        return render_template('/comlist')
    elif request.method == 'POST':
        pass



@cms.route('/course',methods=['GET','POST'])
def course():
    if request.method == 'GET':
        return render_template('/coulist')
    elif request.method == 'POST':
        course_id = request.form['course_id']
        course_name = request.form['course_name']
        do_course(course_id)



# @cms.log('/log',method=['GET','POST'])
# def log():
#     return render_template('log.html')


