import models
from entry import *

def get_course_by_id(course_id):
    return models.find(Course, Course.id == course_id)[0]
