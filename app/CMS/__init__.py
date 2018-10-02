from flask import Blueprint
cms = Blueprint('cms', '__name__')
from . import views
