# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import render_template, request
from . import fontserver


@fontserver.route('/')
def index():
    return render_template('server/index.html')

@fontserver.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['account'] and request.form['password']:
            return request.form['account']
        else:
            error = 'Invalid username/password'
            return error
    # 如果请求访求是 GET 或验证未通过就会执行下面的代码
    return render_template('server/login.html')


@fontserver.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        print(request.form)
        print(request.form['phone'])
        return 'made'
    else:
    # 如果请求访求是 GET 或验证未通过就会执行下面的代码
        return render_template('server/register.html')

