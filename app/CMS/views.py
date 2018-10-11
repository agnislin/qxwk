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


