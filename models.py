# from sshtunnel import SSHTunnelForwarder
# from sqlalchemy import Column, String, Integer,  DateTime, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
#
# mysql_host = "localhost"
# mysql_port = "3306"
# mysql_user = "root"
# mysql_password = ""
# mysql_db = "qxwk"
# ssh_host = "39.108.141.220"
# ssh_port = "22"
# ssh_user = "root"
# ssh_password = "Micouser2018"
#
# Base = declarative_base()
#
# class Account(Base):
#     __tablename__ = 'Account'
#     id = Column(Integer, primary_key=True)
#     email = Column(String(60), nullable=False)
#     phone = Column(String(16))
#     nickname = Column(String(100))
#     password = Column(String(20), nullable=False)
#     time = Column(DateTime)
#
#
# with SSHTunnelForwarder((ssh_host, ssh_port), ssh_username=ssh_user, ssh_password=ssh_password, remote_bind_address=(mysql_host, mysql_port)) as server:
#     assert isinstance(server.start, object)
#     server.start()  # start ssh sever
#     local_port = str(server.local_bind_port)
#     engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(mysql_user,
#                                                                                 mysql_password,
#                                                                                 '127.0.0.1',
#                                                                                 local_port,
#                                                                                 mysql_db),
#                            pool_recycle=1)
#
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     printsession.query(Account).filter(Account.id== 1).all()