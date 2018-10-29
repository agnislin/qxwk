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

@fontserver.route('/')
def comm():
<<<<<<< HEAD
    # models.db.create_all()
    # acc = e.Account(email="1174793398@qq.com", password="1233456", nickname="agnis", phone="10838161238")
    # models.save(acc)
=======
    models.db.create_all()
    # a=e.AdminInfo(
    #         name='root',
    #         password='000000',
    #         picture='jpg/admin.jpg',
    #         whether=True
    #     )
    # models.save(a)
>>>>>>> origin/models

    return render_template('server/comment.html')


@fontserver.route("/nextComments", methods=["POST"])
def next_comments():

    # acc = e.Account(email="1174793398@qq.com", password="1233456", nickname="agnis", phone="10838161238")
    # models.save(acc)
    # 评论
    # class Comment(db.Model):
    #     __tablename__ = 'Comment'
    #     id = db.Column(db.Integer, primary_key=True)
    #     account_id = db.Column(db.Integer, db.ForeignKey('Account.id'))  # 用户ID
    #     video_id = db.Column(db.Integer)  # 视频ID  db.ForeignKey('Video.id')
    #     comment = db.Column(db.String(1000))  # 评论内容
    #     time = db.Column(db.DateTime, default=datetime.now)  # 评论时间

    # comment = e.Comment(account_id=1, video_id=1, comment="hello")
    # models.save(comment)
    # # Get start and end point for posts to generate.
    # #temp
    # # acc = models.db.session.query(e.Account).first()
    # # comm = e.Comment(account_id=123, video_id=2, comment="hello  sqlalchemy")
    # # models.save(comm)
    # # print(models.db.session.query(e.Comment).first().account_id)

    # print(models.find([e.Account, e.Comment], None).first()[0].nickname)

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
<<<<<<< HEAD
    content = request.form.get("content")
    data2 = []
    data2.append(content)
    time.sleep(1)
    return jsonify(data2)
=======
    forum_info = dict()
    forum_info["comment"] = request.form.get("comment")
    forum_info["account_id"] = request.form.get("accountId")

    forum_info["time"] = tl.get_time()
    forum_info.append({})
    return jsonify(forum_info)
>>>>>>> origin/models
