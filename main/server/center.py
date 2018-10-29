from . import mailvertify as m
from flask import render_template, request, session, redirect, url_for
from . import fontserver
from main.server.user_center.account import *

@fontserver.route('/myOrder')
def myOrder():
    uid = get_account()
    if uid:
        username = uid.username if uid.username else (
        uid.email if uid.email else uid.phone)
        return render_template('server/myOrder.html', username=username, course=None)
    else:
        return redirect('login')

@fontserver.route('/myCourse')
def myCourse():
    uid = get_account()
    if uid:
        username = uid.username if uid.username else (
            uid.email if uid.email else uid.phone)
        return render_template('server/myCourse.html', username=username, course=None)
    else:
        return redirect('login')

@fontserver.route('/myRecord')
def myRecord():
    uid = get_account()
    if uid:
        username = uid.username if uid.username else (
            uid.email if uid.email else uid.phone)
        return render_template('server/myRecord.html', username=username, course=None)
    else:
        return redirect('login')
