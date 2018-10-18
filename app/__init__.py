# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask
from app.server import fontserver
from app.CMS import cms
from flask import url_for

app = Flask(__name__)
app.debug = False

app.register_blueprint(fontserver)
app.register_blueprint(cms, url_prefix='/admin')

