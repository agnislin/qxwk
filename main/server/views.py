# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, jsonify, render_template, request
from . import fontserver
import models
import entry as e
import main.tools.tools as tl




@fontserver.route('/comment')
def comm():
    # models.db.create_all()
    acc = e.Account(email="1174793398@qq.com", password="1233456", nickname="agnis", phone="10838161238")
    models.save(acc)

    return render_template('server/comment.html')


@fontserver.route("/nextComments", methods=["POST"])
def next_comments():
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

    account_id = db.Column(db.Integer, db.ForeignKey('Account.id'))  # 用户ID
    video_id = db.Column(db.Integer)  # 视频ID  db.ForeignKey('Video.id')
    comment = db.Column(db.String(1000))  # 评论内容
    time = db.Column(db.DateTime, default=datetime.now)  # 评论时间
@fontserver.route("/forum", methods=["POST"])
def forum():
    forum_info = dict()
    forum_info["comment"] = request.form.get("comment")
    forum_info["account_id"] = request.form.get("accountId")

    forum_info["time"] = time
    forum_info.append({})
    time.sleep(1)
    return jsonify(forum_info)