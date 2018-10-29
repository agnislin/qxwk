
from flask import session
import models
from entry import *


def session_value(key, default=None):
    return session.get(key, default)

def is_login():
    return bool(session_value("account_id"))

def get_account():
    print("get account id = ", get_account_id())
    account = models.db.session.query(Account).filter(Account.id == get_account_id())
    return account.first()

def get_account_id():
    return session_value("account_id", -1)

def get_login_name():
    acc = get_account()
    return acc.phone if acc.phone else acc.email

def paw_sha1(password):
    return password

def find(username):
    account = models.db.session.query(Account).filter(models.db.or_(Account.phone == username, Account.email == username))
    # account = models.find_one(Account, models.db.or_(Account.phone == username or Account.email == username))
    return account[0]
