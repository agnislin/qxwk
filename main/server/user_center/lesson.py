import .account as acc


def get_course_list():
    return acc.get_account().courses

def get_personal_info():
    return models.find(UserInfo, UserInfo.account_id = acc.get_account_id())

def contain_course(course_id):
    pass
