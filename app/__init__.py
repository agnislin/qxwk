# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask
from app.server import fontserver
from app.CMS import cms
import models


app = Flask(__name__)

class Config(object):
    # debug
    DEBUG = False

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/qxwk"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 7  # session 的有效期，单位是秒


app.config.from_object(Config)
app.debug = True

app.register_blueprint(fontserver)
app.register_blueprint(cms, url_prefix='/admin')


models.models(app)
