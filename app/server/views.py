from flask import render_template
from . import fontserver

@fontserver.route('/')
def index():
    return render_template('server/index.html')