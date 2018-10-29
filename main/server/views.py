# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, jsonify, render_template, request
from . import fontserver
import models
import entry as e
import main.tools.tools as tl
from .auth import log_req

# __tablename__ = 'Course'
# id = db.Column(db.Integer, primary_key=True)
# lecturer = db.Column(db.String(20))  # 讲师
# course = db.Column(db.String(50), unique=True)  # 课程名称
# introduction = db.Column(db.String(2048))  # 课程介绍
# cost = db.Column(db.Float, nullable=False)  # 课程售价
# type = db.Column(db.Integer)  # 课程分类
# date = db.Column(db.Integer)  # 课程周期
# cover = db.Column(db.String(100))  # 封面

@fontserver.route('/')
def comm():
    cour = models.find(e.Course)[0]

    return render_template('server/comment.html', course = cour, username=log_req())


@fontserver.route("/nextComments", methods=["POST"])
def next_comments():

    # print(models.find(e.Account, None).first().nickname)
    # #
    # # print(models.find([e.Account, e.Comment], e.Account.id == e.Comment.account_id)[1][1].comment)
    #
    # start = int(request.form.get("start") or 0)
    # end = int(request.form.get("end") or (start + 9))
    #
    # # Generate list of posts.
    # data = []
    # for i in range(start, end + 1):
    #     data.append("评论%s" % i)

    # Artificially delay speed of response.
    acc = 1
    vid = 1

    data = []
    coms = models.find(e.Comment,e.Comment.video_id == vid)
    for comment in coms:
        account = models.find(e.UserInfo,e.UserInfo.account_id == comment.account_id)[0]
        data.append((account, comment))

    # Return list of posts.
    return render_template('server/forum.html', forum_list =data)

    # account_id = db.Column(db.Integer, db.ForeignKey('Account.id'))  # 用户ID
    # video_id = db.Column(db.Integer)  # 视频ID  db.ForeignKey('Video.id')
    # comment = db.Column(db.String(1000))  # 评论内容
    # time = db.Column(db.DateTime, default=datetime.now)  # 评论时间


@fontserver.route("/forum", methods=["POST"])
def forum():
    forum_info = dict()
    forum_info["comment"] = request.form.get("comment")
    forum_info["account_id"] = request.form.get("accountId")

    forum_info["time"] = tl.get_time()
    forum_info.append({})
    return jsonify(forum_info)
