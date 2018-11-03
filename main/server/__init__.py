from flask import Blueprint
fontserver = Blueprint('server', '__name__')
from . import views
# from . import auth
from . import mailvertify
from . import center
