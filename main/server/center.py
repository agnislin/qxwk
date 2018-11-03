from . import mailvertify as m
from flask import render_template, request, session, redirect, url_for
from . import fontserver
from main.server.user_center.account import *

@fontserver.route('/myOrder')
def myOrder():
    if is_login:
        courses_1 = models.find(Account, Account.id == 1)[0].courses
        
        return render_template('server/myOrder.html', username=get_login_name(), course=courses_1)
    else:
        return redirect('login')

@fontserver.route('/myCourse')
def myCourse():
    if is_login:
        courses_1 = models.find(Account, Account.id == 1)[0].courses
        return render_template('server/myCourse.html', username=get_login_name(), course=courses_1)
    else:
        return redirect('login')

@fontserver.route('/myRecord')
def myRecord():
    if is_login:
        courses_1 = models.find(Account, Account.id == 1)[0].courses
        return render_template('server/myRecord.html', username=get_login_name(), course=courses_1)
    else:
        return redirect('login')
