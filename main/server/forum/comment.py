# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import models
from entry import *
from main.server.user_center.account import *


def get_comment_by_video_id(video_id, limit=1):
    data = list()
    coms = models.find(Comment, Comment.video_id == video_id, limit)

    for comment in coms:
        try:
            account = models.find(UserInfo, UserInfo.account_id == comment.account_id)[0]
            data.append((account, comment))
        except Exception as e:
            print("get_comment_by_video_id: list index out of range")
            
    print("get_comment_by_video_id", data)
    return data


def save_comment(video_id, content):
    data = dict()
    data["account_id"] = get_account_id()
    data["video_id"] = video_id
    data["comment"] = content
    c = Comment(**data)
    models.save(c)
    return c
