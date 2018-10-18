from flask import Blueprint
fontserver = Blueprint('server', '__name__')
from . import views


