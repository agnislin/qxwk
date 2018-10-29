# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import mailvertify as m
from flask import render_template, request, session, redirect, url_for
from . import fontserver
import models
from entry import Account
from entry import db
import random
# from dysms_python import demo_sms_send
#dysms_python放到C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Lib\site-packages
import json

def log_req():
    '''用户没有登录返回False，已登录返回Account对象'''
    try:
        uid = session['UID']
    except:
        return False
    else:
        return Account.query.filter(Account.id == uid).first()


@fontserver.route('/')
def index():
    acc = log_req()
    if acc:
        return render_template('server/index.html', username=True)
    else:
        return render_template('server/index.html')
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
        account = request.form.get('account')
        password = request.form.get('password')
        if account.isdigit():
            phone = Account.query.filter(Account.phone == account).first()
            if phone:
                if phone.password == password:
                    session['UID'] = phone.id
                    return 'redirect'
                else:
                    return '密码错误！'
            else:
                return '该账号尚未注册！'
        else:
            mail = Account.query.filter(Account.email == account).first()
            if mail:
                if mail.password == password:
                    session['UID'] = mail.id
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


@fontserver.route('/register', methods=['GET','POST'])
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
            s = ''.join( random.sample(['1', '2', '3', '4', '5',
                           '6', '7', '8', '9', '0'], 6))
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


#/vertify/1653075632@qq.com+asdf12
# register_book['1653075632@qq.com'] = {'password': '123456', 'randomcode': 'asdf12'}

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
