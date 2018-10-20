# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from entry import *


# 此函数于控制SQLAlchemy与一个Flask应用程序的集成
def set_app(application):
    # 初始化应用程序以供此数据库设置使用。切勿在未以该方式初始化的应用程序的上下文中使用数据库，否则发生连接将泄漏
    db.init_app(application)


# 插入一条数据
def save(obj):
    ''' 插入一条数据obj 为表类调用的返回结果
    如
    obj= Account(
        id = 1
    )
    '''
    try:
        db.session.add(obj)
        db.session.commit()
        return True
    except Exception as a:
        print(a)
        db.session.rollback()
        return False


# 插入多条数据
def save_all(list_obj):
    '''插入多条数据 list_obj 为表类调用的返回结果的列表
    如
    list_obj= [Account(id = 1),Couse(id=2)]
    '''
    l = []
    for i in list_obj:
        try:
            db.session.add(i)
            db.session.commit()
        except:
            db.session.rollback()
            l.append(i)
    return l


# 删除一条数据
def remove(class_type, obj):
    '''删除一条数据'''
    try:
        res = db.find_one(class_type, obj)
        db.session.delete(res)
        db.session.commit()
        return True
    except:
        db.session.rollback()


# 删除满足条件的多条全部数据
def remove_all(class_type, list_obj):
    '''删除满足条件的多条全部数据'''
    for i in list_obj:
        try:
            res = db.find_one(class_type, i)
            db.session.delete(res)
            db.session.commit()
            return True
        except:
            db.session.rollback()


# # 查询一条条件为字符串 如"name='guokaiqiang',age=25"
# def find_one(class_type, conditionn):
#     return db.session.query(exec("Account, Video"))
#
#
# def get(self, class_type, value):
#     pass


# x为要查询的条数  n为字段名加.desc()字符串的  如 "User.desc()"
def find(entry, condition=None, x=-1, n=-1):
    '''x为要查询的条数  n为字段名加.desc()字符串的  如 "User.desc()"'''
    try:
        if type(entry) in [list, tuple, set]:
            # print("多表 [", ",".join([t.__name__ for t in entry]), "]")
            res = db.session.query(*entry)
        else:
            # print("单表")
            res = db.session.query(entry)

        if condition is None:
            if x == -1:
                if n == -1:
                    return res.first()
                else:
                    return res.order_by(eval(n))
            else:
                if n == -1:
                    return res.limit(x).all()
                else:
                    return res.order_by(eval(n)).limit(x).all()
        else:
            res = res.filter(condition)

            if x == -1:
                if n == -1:
                    return res.frist()
                else:
                    return res.order_by(eval(n))
            else:
                if n == -1:
                    return res.limit(x).all()
                else:
                    return res.order_by(eval(n)).limit(x).all()
    except:
        return False

def change(alternative,field,entry, condition=None):
    '''alternative需要更改成什么(字符串),entry要先查找的记录, condition条件,field.要更改的字段'''

    res = find(entry,condition)
    res.field = alternative

def contain( entry, condition=None):

    '''判断'''
    try:
        a = find(entry,condition)
        if a:
            return True
    except:
        return False

# def find(entry, condition=None, order_col=None, limit=-1):
#     if type(entry) in [list, tuple, set]:
#         print("多表 [", ",".join([t.__name__ for t in entry]), "]")
#         res = db.session.query(*entry)
#     else:
#         print("单表", entry.__name__)
#         res = db.session.query(entry)
#
#     if condition is None:
#         return res
#         print("无条件查找")
#     else:
#         print("有条件查找", condition)
#         res = res.filter(condition)
#
#     if order_col == None:
#         if limit == -1:
#             return res
#         else:
#             return res.order_by(eval(limit))
#     else:
#         if limit == -1:
#             return res.limit(order_col).all()
#         else:
#             return res.order_by(eval(limit)).limit(order_col).all()
