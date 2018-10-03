# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask
from app.server import fontserver
from app.CMS import cms
from flask import url_for

app = Flask(__name__)
app.debug = True

app.register_blueprint(fontserver)
app.register_blueprint(cms, url_prefix='/admin')

# STATIC_URL_ROOT = '//127.0.0.1:5000/'
#
# @app.context_processor
# def override_url_for():
#     return dict(url_for=static_url_for)
#
# def static_url_for(endpoint, **values):
#     if endpoint == 'static':
#         filename = values.get('filename', None)
#         if filename:
#             file_path = STATIC_URL_ROOT + filename
#             return file_path
#     else:
#         return url_for(endpoint, **values)
