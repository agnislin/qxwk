# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from . import mailvertify as m
from flask import render_template, request
from . import fontserver
import models
import entry as e


@fontserver.route('/account')
def index():
    return render_template('server/index.html', username=None)


@fontserver.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('server/login.html')
    elif request.method == 'POST':
        account = request.form.get('account')
        password = request.form.get('password')
        # if "///查不到数据"：
        #     return '账号不存在'
        # elif "///查不到密码"：
        #     return '密码错误！'
        
register_book = {}


@fontserver.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('server/register.html')
    elif request.method == 'POST':
        if request.form.get('phone'):
            pass
        elif request.form.get('mail'):
            try:
                mail = request.form['mail']
                password = request.form['password']
            except:
                return render_template('server/register.html')
            randomcode = m.randomcode()
            register_book[mail] = {'password': password, 'timecode': round(
                time.time()), 'randomcode': randomcode}
            if m.sendmail(mail, m.makemail(mail, randomcode)):
                return '邮件已发送，若未收到，请检查拦截设置'
            else:
                return '邮件发送失败！请检查邮箱是否正确'


@fontserver.route('/vertify/<peramen>')
def vertify(peramen):
    mail = peramen.split('&&')[0]
    randomcode = peramen.split('&&')[1]
    a = register_book.get(account)['timecode']
    if a is None:
        pass
    else:
        if time.time()-a < 600 and register_book.get(account)['randomcode'] == randomcode:
            # password = register_book[account]['password']
            #添加account,password数据库
            print(register_book[account])
            return "success!"
        else:
            return '邮件过期'


@fontserver.route('/get')
def get():
    print(register_book)

