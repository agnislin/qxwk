# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_session import Session
from flask_script import Manager
from sqlalchemy import text

# app = Flask(__name__,
#             instance_path="E:\\workspace\\pycharm\\demo\\config_private",
#             instance_relative_config=True)


db = SQLAlchemy()


def models(application):
    db.init_app(application)


course_sel = db.Table("course_sel",
                      db.Column("account_id", db.Integer,
                                db.ForeignKey("Account.id")),
                      db.Column("course_id", db.Integer, db.ForeignKey("Course.id")))


class Account(db.Model):
    __tablename__ = 'Account'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False, unique=True)  # 邮箱
    phone = db.Column(db.String(16))  # 手机号
    nickname = db.Column(db.String(20))  # 昵称
    password = db.Column(db.String(32), nullable=False)  # 密码
    time = db.Column(db.DateTime)  # 注册时间
    courses = db.relationship("Course", secondary=course_sel, backref=db.backref(
        "Account", lazy="dynamic"), lazy="dynamic")


# 课程大纲
class Course(db.Model):
    __tablename__ = 'Course'
    id = db.Column(db.Integer, primary_key=True)
    lecturer = db.Column(db.String(20))  # 讲师
    course = db.Column(db.String(50), unique=True)  # 课程名称
    introduction = db.Column(db.String(2048))  # 课程介绍
    cost = db.Column(db.Float, nullable=False)  # 课程售价
    classl = db.Column(db.Integer)  # 课程分类
    date = db.Column(db.Integer)  # 课程周期
    cover = db.Column(db.String(100))  # 封面

# _________________________________--------------------------------------

# 个人信息


class User_info(db.Model):  # 继承生成的orm基类
    __tablename__ = 'User_info'  # 表名
    id = db.Column(db.Integer, primary_key=True)
    Account_id = db.Column(db.Integer, db.ForeignKey("Account.id"))
    name = db.Column(db.String(16), nullable=False)  # 姓名
    sex = db.Column(db.String(10))  # 性别
    birthday = db.Column(db.Date)  # 生日
    occupation = db.Column(db.String(15))  # 职业
    # 喜欢那一门课程
    interest = db.Column(db.Integer)
    introduction = db.Column(db.String(300))  # 个人介绍
    picture = db.Column(db.String(150))  # 头像地址

# 创建地址表


class Address(db.Model):  # 继承生成的orm基类
    __tablename__ = "Address"  # 表名
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User_info.id"))
    province = db.Column(db.String(30))
    city = db.Column(db.String(30))
    county = db.Column(db.String(30))
    detailed = db.Column(db.String(100))
# unique=True#设置当前字段不可重复


# 课程视频
class Video(db.Model):
    __tablename__ = 'Video'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("Course.id"))
    name = db.Column(db.String(30), nullable=False)  # 视频名称
    addr = db.Column(db.String(100), nullable=False)  # 视频地址
    introduction = db.Column(db.String(1000))  # 课程简介


# 首页视频
class Home_video(db.Model):
    __tablename__ = 'Home_video'
    id = db.Column(db.Integer, primary_key=True)
    Course_id = db.Column(db.Integer, nullable=False)  # 课程ID
    slogan = db.Column(db.String(300), nullable=False)  # 宣传标语


# 评论
class Comment(db.Model):
    __tablename__ = 'Comment'
    id = db.Column(db.Integer, primary_key=True)
    Account_id = db.Column(db.Integer, db.ForeignKey('Account.id'))  # 用户ID
    Video_id = db.Column(db.Integer)  # 视频ID  db.ForeignKey('Video.id')
    comment = db.Column(db.String(1000))  # 评论内容
    time = db.Column(db.DateTime)  # 品论时间

# 平台通知


class Platform_meg(db.Model):
    __tablename__ = 'Platform_meg'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))  # 内容
    date = db.Column(db.DateTime)  # 时间


# 课程通知
class Course_meu(db.Model):
    __tablename__ = 'Course_meu'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))  # 内容
    date = db.Column(db.DateTime)  # 时间
    Course_id = db.Column(db.Integer, nullable=False)  # 课程ID
    Account_id = db.Column(db.Integer, nullable=False)  # 账户ID

# 反馈信息


class Feedback(db.Model):
    __tablename__ = 'Feedback'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)  # 账户邮箱
    feedback = db.Column(db.String(1000))  # 反馈信息
    date = db.Column(db.DateTime)  # 时间

# 学习记录


class Learning_log(db.Model):
    __tablename__ = 'Learning_log'
    id = db.Column(db.Integer, primary_key=True)
    Course_id = db.Column(db.Integer, nullable=False)  # 课程ID
    Video_id = db.Column(db.Integer, nullable=False)  # 视频ID
    Played = db.Column(db.Time)  # 已播放时长
    date = db.Column(db.DateTime)  # 时间


# 笔记
class Lote(db.Model):
    __tablename__ = 'Lote'
    id = db.Column(db.Integer, primary_key=True)
    Account_id = db.Column(db.Integer, nullable=False)  # 账户ID
    Video_id = db.Column(db.Integer, nullable=False)  # 视频ID
    content = db.Column(db.String(3000))  # 内容
    date = db.Column(db.DateTime)  # 时间
    discuss_id = db.Column(db.Integer, nullable=False)  # 讨论ID也是一个账户ID
    praise = db.Column(db.Integer, nullable=False)  # 赞

# 管理员信息


class Admininfor(db.Model):
    __tablename__ = 'Admininfor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)  # 账户
    password = db.Column(db.String(20), nullable=False)  # 密码
    date = db.Column(db.DateTime)  # 时间
    picture = db.Column(db.String(100))  # 头像地址
    whether = db.Column(db.Boolean)
# 操作记录


class Operation_log(db.Model):
    __tablename__ = 'Operation_log'
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(60))
    content = db.Column(db.String(1000))  # 内容
    date = db.Column(db.DateTime)  # 时间
    admininfor_id = db.Column(db.Integer, nullable=False)


# 选课
class Lect(db.Model):
    __tablename__ = 'Lect'
    id = db.Column(db.Integer, primary_key=True)
    Account_id = db.Column(db.Integer, nullable=False)  # 账户ID
    Course_id = db.Column(db.Integer, nullable=False)  # 课程ID
    Lectdate = db.Column(db.DateTime)  # 时间
# 新增数据


class ModelBase(object):

    def __init__(self):
        self.session = db.Session()
# 插入一条数据

    def save(self, obj):
        try:
            self.session.add(obj)
            self.session.commit()
        except:
            self.session.rollback()
            return False
# 插入多条数据

    def saveAll(self, listObj):
        l = []
        for i in listObj:
            try:
                self.session.add(i)
                self.session.commit()
            except:
                self.session.rollback()
                l.append(i)
        return l

    def remove(self, class_type, obj):
        try:
            res = self.findOne(class_type, obj)
            self.session.delete(res)
            self.session.commit()
        except:
            self.session.rollback()

    def removeall(self,class_type, listObj):
        for i in listObj:
            try:
                res = self.findOne(class_type, i)
                self.session.delete(res)
                self.session.commit()
            except:
                self.session.rollback()

    def findOne(self, class_type, tiaojian):  # 查询一条条件为字符串如"name='guokaiqiang',age=25"
        return self.session.query(eval(class_type)).filter(text(tiaojian)).first()

    def get(self, class_type, vlaue):
        pass

    def find(self, class_type, tiaojian, x=-1, n=-1):  # x为条数
        # .filter(text(tiaojian)).all()
        res = self.session.query(eval(class_type))
        res = res.filter(text(tiaojian))
        if x == -1:
            if n == -1:
                return res
            else:
                # n为字符串的字段名加.desc()  如 "User.desc()"
                return res.order_by(eval(n))
        else:
            if n == -1:
                return res.limit(x).all()
            else:
                # n为字符串的字段名加.desc()  如 "User.desc()"
                return res.order_by(eval(n)).limit(x).all()

    def update(self, obj):
        pass

    def contain(self, class_type, tiaojiao):
        pass

    def sort(self, find, list_column, desc=True):
        pass
