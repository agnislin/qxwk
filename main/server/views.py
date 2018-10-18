# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, jsonify, render_template, request
from . import fontserver
import time
import models
import entry as e


@fontserver.route('/')
def comm():
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

    comment = e.Comment(account_id=1, video_id=1, comment="hello")
    models.save(comment)
    # Get start and end point for posts to generate.
    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9))

    # Generate list of posts.
    data = []
    for i in range(start, end + 1):
        data.append("评论%s" % i)

    # Artificially delay speed of response.
    time.sleep(1)

    # Return list of posts.
    return jsonify(data)


@fontserver.route("/forum", methods=["POST"])
def forum():
    content = request.form.get("content")
    data2 = []
    data2.append(content)
    time.sleep(1)
    return jsonify(data2)