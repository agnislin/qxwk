
from flask import session
import models
from entry import *


accounts = dict()

def session_value(key, default=None):
    return session.get(key, default)

def is_login():
    return bool(session_value("account_id"))

def get_account():
    acc_id = get_account_id()
    try:
        return accounts.get(get_account_id(), models.find(Account, Account.id==get_account_id())[0])
    except Exception:
        return None

def get_account_id():
    return session_value("account_id", None)

def get_login_name():
    acc = get_account()
    try:
        return acc.phone if acc.phone else acc.email
    except Exception:
        return None


def paw_sha1(password):
    return password

def find(username):
    account = models.db.session.query(Account).filter(models.db.or_(Account.phone == username, Account.email == username))[0]
    accounts[account.id] = account
    print(account)
    return account

def get_user_info():
    return models.find(UserInfo, UserInfo.account_id == get_account_id())[0]
