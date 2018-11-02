# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, jsonify, render_template, request
from . import fontserver
from main.server.forum.comment import *
from main.server.video.search import *
from main.server.user_center.account import *


@fontserver.route('/video')
def comm():
    if request.method == "GET":
        course_id = request.args["course_id"]
        print(course_id)
        cour = get_course_by_id(course_id)
        videos = get_videos_by_id(course_id)
        print(videos)
        return render_template('server/comment.html', course=cour, videos=videos, username=get_login_name())


@fontserver.route("/nextComments", methods=["POST"])
def next_comments():
    data = get_comment_by_video_id(1, limit=8)
    return render_template('server/forum.html', forum_list=data)


@fontserver.route("/forum", methods=["POST"])
def forum():
    vid = request.form.get("video_id")
    content = request.form.get("content")

    comm_obj = save_comment(vid, content)
    user = get_user_info()

    return render_template('server/forum.html', forum_list=[(user, comm_obj)])


@fontserver.route('/KCJieShao/<int:course_id>')
def KCJieShao(course_id):
    data = models.find(Course,Course.id ==course_id)[0]
    data1= models.find(Video,Video.course_id ==course_id)
    print(data)
    return render_template('server/KCJieShao.html', course=data,videos=data1)




@fontserver.route("/KCJieShao/<menu>")
def menu_views(menu):
    if menu =='ML':
        print(menu)

    return "dsfdfs"


@fontserver.route('/')
def home():
    data = models.find(Course,Course.price > 0,limit=8)
    datafree = models.find(Course,Course.price ==0,limit=8)
    data2 = models.find(HomeVideo,limit=6)
    return render_template('server/index.html', course_list=data, free_course_list=datafree, username=get_login_name(), rollcover=data2)
