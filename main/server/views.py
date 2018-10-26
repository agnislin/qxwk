# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, jsonify, render_template, request
from . import fontserver
import models
import entry as e
import main.tools.tools as tl

# __tablename__ = 'Course'
# id = db.Column(db.Integer, primary_key=True)
# lecturer = db.Column(db.String(20))  # 讲师
# course = db.Column(db.String(50), unique=True)  # 课程名称
# introduction = db.Column(db.String(2048))  # 课程介绍
# cost = db.Column(db.Float, nullable=False)  # 课程售价
# type = db.Column(db.Integer)  # 课程分类
# date = db.Column(db.Integer)  # 课程周期
# cover = db.Column(db.String(100))  # 封面

@fontserver.route('/comment')
def comm():
    # models.db.create_all()
    # acc = e.Account(email="2274793398@qq.com", password="2223456", nickname="linnis", phone="22838161238")
    # course = e.Course(lecturer="li lin", course="java web", introduction="web develop", cost=1000, type=123123)
    # acc.courses = [course]
    # models.save(acc)
    return render_template('server/comment.html')


@fontserver.route("/nextComments", methods=["POST"])
def next_comments():
    # Get start and end point for posts to generate.
    #temp
    # acc = models.db.session.query(e.Account).first()
    # comm = e.Comment(account_id=123, video_id=2, comment="hello  sqlalchemy")
    # models.save(comm)
    # print(models.db.session.query(e.Comment).first().account_id)

    print(models.find(e.Account, None).first().nickname)
    #
    # print(models.find([e.Account, e.Comment], e.Account.id == e.Comment.account_id)[1][1].comment)

    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9))

    # Generate list of posts.
    data = []
    for i in range(start, end + 1):
        data.append("评论%s" % i)

    # Artificially delay speed of response.

    # Return list of posts.
    return jsonify(data)

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
