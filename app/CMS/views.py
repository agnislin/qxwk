from flask import render_template
from . import cms

@cms.route('/')
def index():
    return render_template('cms/index.html')