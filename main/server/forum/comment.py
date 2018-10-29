# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask_sqlalchemy import SQLAlchemy
import models
from entry import *
import main.tools.tools as tl
# from .auth import seesion_value


def get_comment_by_video_id(video_id):

    data = []
    coms = models.find(e.Comment,e.Comment.video_id == vid)
    for comment in coms:
        account = models.find(e.UserInfo,e.UserInfo.account_id == comment.account_id)[0]
        data.append((account, comment))

    # Return list of posts.
    return render_template('server/forum.html', forum_list =data)
