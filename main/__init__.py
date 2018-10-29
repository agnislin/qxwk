# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask
from .server import fontserver
from .CMS import cms
import models


# 接收应用程序包名, 使用__name__而不是'__main__', 因为它的值是区分作为应用程序启动还是作为模块导入的
app = Flask(__name__)
# app = Flask("main")

app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/qxwk"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = b'\x1cf\x9a\xd5\xcd\xfc\x85\xf9F\4\x9b\xb9\xea\xfex?\xd3N\xbf\xf9MVV\x13'
app.register_blueprint(fontserver)
app.register_blueprint(cms, url_prefix='/admin')

# 将flask_sqlalchemy.SQLAlchemy附加到Flask
models.set_app(app)

# session
# SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
# SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
# SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
# PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 7  # session 的有效期，单位是秒


