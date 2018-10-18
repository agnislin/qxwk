from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 创建一个未配置的SQLAlchemy对象
db = SQLAlchemy()

# 用户选课关系帮助程序表
course_sel = db.Table("course_sel",
                      db.Column("account_id", db.Integer, db.ForeignKey("Account.id")),
                      db.Column("course_id", db.Integer, db.ForeignKey("Course.id")),
                      db.Column('data', db.DateTime, nullable=False))


class Account(db.Model):
    __tablename__ = 'Account'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False, unique=True)  # 邮箱
    phone = db.Column(db.String(16))  # 手机号
    nickname = db.Column(db.String(20))  # 昵称
    password = db.Column(db.String(32), nullable=False)  # 密码
    time = db.Column(db.DateTime, default=datetime.now)  # 注册时间
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
    type = db.Column(db.Integer)  # 课程分类
    date = db.Column(db.Integer)  # 课程周期
    cover = db.Column(db.String(100))  # 封面


# 个人信息
class UserInfo(db.Model):  # 继承生成的orm基类
    __tablename__ = 'User_info'  # 表名
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey("Account.id"))
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


# 课程视频
class Video(db.Model):
    __tablename__ = 'Video'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("Course.id"))
    name = db.Column(db.String(30), nullable=False)  # 视频名称
    addr = db.Column(db.String(100), nullable=False)  # 视频地址
    introduction = db.Column(db.String(1000))  # 课程简介


# 首页视频
class HomeVideo(db.Model):
    __tablename__ = 'Home_video'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, nullable=False)  # 课程ID
    slogan = db.Column(db.String(300), nullable=False)  # 宣传标语


# 评论
class Comment(db.Model):
    __tablename__ = 'Comment'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('Account.id'))  # 用户ID
    video_id = db.Column(db.Integer)  # 视频ID  db.ForeignKey('Video.id')
    comment = db.Column(db.String(1000))  # 评论内容
    time = db.Column(db.DateTime, default=datetime.now)  # 评论时间


# 平台通知
class PlatformMeg(db.Model):
    __tablename__ = 'Platform_meg'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))  # 内容
    date = db.Column(db.DateTime, default=datetime.now)  # 时间


# 课程通知
class CourseMeg(db.Model):
    __tablename__ = 'Course_meg'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))  # 内容
    date = db.Column(db.DateTime, default=datetime.now)  # 时间
    course_id = db.Column(db.Integer, nullable=False)  # 课程ID
    account_id = db.Column(db.Integer, nullable=False)  # 账户ID


# 反馈信息
class Feedback(db.Model):
    __tablename__ = 'Feedback'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)  # 账户邮箱
    feedback = db.Column(db.String(1000))  # 反馈信息
    date = db.Column(db.DateTime, default=datetime.now)  # 时间


# 学习记录
class Learning_log(db.Model):
    __tablename__ = 'Learning_log'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, nullable=False)  # 课程ID
    video_id = db.Column(db.Integer, nullable=False)  # 视频ID
    played = db.Column(db.Time)  # 已播放时长
    date = db.Column(db.DateTime, default=datetime.now)  # 时间


# 笔记
class Note(db.Model):
    __tablename__ = 'Note'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, nullable=False)  # 账户ID
    video_id = db.Column(db.Integer, nullable=False)  # 视频ID
    content = db.Column(db.String(3000))  # 内容
    date = db.Column(db.DateTime, default=datetime.now)  # 时间
    discuss_id = db.Column(db.Integer, nullable=False)  # 讨论ID也是一个账户ID
    praise = db.Column(db.Integer, nullable=False)  # 赞


# 管理员信息
class AdminInfo(db.Model):
    __tablename__ = 'Admin_info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)  # 账户
    password = db.Column(db.String(20), nullable=False)  # 密码
    date = db.Column(db.DateTime, default=datetime.now)  # 时间
    picture = db.Column(db.String(100))  # 头像地址
    whether = db.Column(db.Boolean)


# 操作记录
class OperationLog(db.Model):
    __tablename__ = 'Operation_log'
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(60))
    content = db.Column(db.String(1000))  # 内容
    date = db.Column(db.DateTime, default=datetime.now)  # 时间
    admin_info = db.Column(db.Integer, db.ForeignKey('Admin_info.id'))

