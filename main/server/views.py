# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, jsonify, render_template, request
from . import fontserver

import main.server.forum.comment
import models
from entry import *


@fontserver.route('/comment')
def comm():
    cour = get_course_by_id(1)

    acc = get_account()
    print(cour, acc)
    return render_template('server/comment.html', course=cour, username=acc)


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


@fontserver.route('/KCJieShao')
def KCJieShao():
    data = models.find(Course,Course.id == 1)[0]
    print(data)
    return render_template('server/KCJieShao.html', course=data) 




@fontserver.route("/KCJieShao/<menu>")
def menu_views(menu):
    if menu =='ML':
        print(menu)
    
    return "dsfdfs"


