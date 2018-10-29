from . import mailvertify as m
from flask import render_template, request, session, redirect, url_for
from . import fontserver
import models
from entry import Account
from entry import db
from .auth import log_req

@fontserver.route('/myOrder')
def myOrder():
    uid = log_req()
    if uid:
        username = uid.nickname if uid.nickname else (
        uid.email if uid.email else uid.phone)
        return render_template('server/myOrder.html', username=username, course=None)
    else:
        return redirect('login')
@fontserver.route('/myCourse')
def myCourse():
    uid = log_req()
    if uid:
        username = uid.nickname if uid.nickname else (
            uid.email if uid.email else uid.phone)
        return render_template('server/myCourse.html', username=username, course=None)
    else:
        return redirect('login')

@fontserver.route('/myRecord')
def myRecord():
    uid = log_req()
    if uid:
        username = uid.nickname if uid.nickname else (
            uid.email if uid.email else uid.phone)
        return render_template('server/myRecord.html', username=username, course=None)
    else:
        return redirect('login')
