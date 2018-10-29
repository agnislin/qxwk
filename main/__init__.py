from __future__ import unicode_literals
from flask import Flask
<<<<<<< HEAD
from main.server import fontserver
from sshtunnel import SSHTunnelForwarder
from main.CMS import cms
=======
from .server import fontserver
from sshtunnel import SSHTunnelForwarder
from .CMS import cms
>>>>>>> origin/models
import models

# 接收应用程序包名, 使用__name__而不是'__main__', 因为它的值是区分作为应用程序启动还是作为模块导入的
app = Flask(__name__)
# app = Flask("main")

app.debug = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://nlikes:123456@39.108.141.220:3306/qxwk"
app.register_blueprint(fontserver)
app.register_blueprint(cms, url_prefix='/admin')

ssh_host = "39.108.141.220"
ssh_port = 22
ssh_user = "root"
ssh_password = "Micouser2018"
mysql_host = "localhost"
mysql_port = 3306

with SSHTunnelForwarder(
    (ssh_host, ssh_port),
    ssh_username=ssh_user,
    ssh_password=ssh_password,
    remote_bind_address=(mysql_host, mysql_port)
) as server:
    # ssh通道服务启动
    server.start()
    local_port = str(server.local_bind_port)

    # 将flask_sqlalchemy.SQLAlchemy附加到Flask
<<<<<<< HEAD
    models.set_app(app)
=======
    models.set_app(app)
>>>>>>> origin/models
