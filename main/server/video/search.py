import models
from entry import *

def get_course_by_id(course_id):
    return models.find(Course, Course.id == course_id)[0]

def get_videos_by_course_id(course_id):
    return models.find(Video, Video.course_id == course_id)

def get_video(video_id):
    return models.find(Video, Video.id == video_id)
