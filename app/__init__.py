from flask import Flask
from app.server import fontserver
from app.CMS import cms

app = Flask(__name__)
app.debug = True

app.register_blueprint(fontserver)
app.register_blueprint(cms,url_prefix='/admin')