# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import mailvertify as m
from flask import render_template, request, session, redirect, url_for
from . import fontserver
from main.server.user_center.account import *
from entry import Account
from entry import db
import random
import json



# @fontserver.route('/')
# def index():
#     if is_login():
#         return render_template('server/index.html', username=True)
#     else:
#         return render_template('server/index.html')

# @fontserver.route('/')
# def index():
#     if session.get('UID'):
#         acc = Account.query.filter(Account.id == session['UID']).first()
#         if acc:
#             return render_template('server/index.html', username=acc.nickname if acc.nickname else (acc.email if acc.email else acc.phone))
#     else:
#         return render_template('server/index.html')


@fontserver.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('server/login.html')
    elif request.method == 'POST':
        username = request.form.get('account')
        password = request.form.get('password')
        account = find(username)
        # print(account)
        # print(account.password)

        if account:
            if account.password == paw_sha1(password):
                session['account_id'] = account.id
                return 'redirect'
            else:
                return '密码错误!'
        else:
            return '该账号尚未注册！'





@fontserver.route('/logout')
def logout():
    session.clear()
    return render_template('server/login.html')

register_book = {}


@fontserver.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('server/register.html')
    elif request.method == 'POST':
        # -----手机
        if request.form.get('getdyc'):
            phnum = request.form.get('getdyc')
            phnum1 = Account.query.filter(Account.phone == phnum).first()
            if phnum1:
                return "该账号已经存在！直接登录吧！"
            s = ''.join( random.sample("0123456789", 6))
            __business_id = demo_sms_send.uuid.uuid1()
            params = "{\"code\":%s}"%s
            result = demo_sms_send.send_sms(__business_id, int(phnum),
                           "千禧微课", "SMS_148830034", params)
            result = json.loads(result.decode())
            if result["Code"] == "OK":
                register_book[phnum] = {'randomcode':s}
                return '验证码已发送，请注意查收'
            else:
                print(result)
                return '非法手机号'

        elif request.form.get('phone'):
            phone = request.form.get('phone')
            password = request.form.get('password')
            dynamincode = request.form['dynamincode']
            try:
                if dynamincode == register_book[phone]['randomcode']:
                    acc1 = Account(phone=phone, password=password)
                    db.session.add(acc1)
                    db.session.commit()
                else:
                    return '验证码错误！'
            except KeyError:
                return '请先获取验证码！'
            else:
                uid = Account.query.filter(Account.phone == phone).first()
                session['UID'] = uid.id
                return 'redirect'
            # ------手机

        elif request.form.get('mail'):
            mail = request.form['mail']
            password = request.form['password']
            email = Account.query.filter(Account.email == mail).first()
            if email:
                return "该账号已经存在！直接登录吧！"
            elif mail in register_book:
                return '邮件已发送'
            else:
                randomcode = m.randomcode()
                register_book[mail] = {'password': password, 'randomcode': randomcode}
                if m.sendmail(mail, m.makemail(mail, randomcode)):
                    return '邮件已发送'
                else:
                    return '邮件发送失败！请检查邮箱是否正确'



@fontserver.route('/get')
def get():
    print(register_book)

@fontserver.route('/vertify/<peramen>', methods= ['get'])
def vertify(peramen):
    if m.vertify(peramen, register_book):
        email = peramen.split('+')[0]
        password = register_book[email]['password']
        acc1 = Account(email=email, password=password)
        db.session.add(acc1)
        db.session.commit()
        return '验证成功，<a href = "http://127.0.0.1:5000/login">点击登录</a>'
    else:
        return '邮件已失效！'
