from django.test import TestCase
from api import models
# Create your tests here.


# 作业：
# 一、准备工作：
# 1.
# 通过admin对13张表录入数据
# 2.
# ORM练习
# a.查看所有学位课并打印学位课名称以及授课老师
#     ret = models.DegreeCourse.objects.all()
#     print(ret)
#
# b.查看所有学位课并打印学位课名称以及学位课的奖学金
#
# c.展示所有的专题课
# models.Course.objects.filter(degree_course__isnull=True)
#
# d.查看id = 1
# 的学位课对应的所有模块名称
#
# e.获取id = 1
# 的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
#
# f.获取id = 1
# 的专题课，并打印该课程相关的所有常见问题
#
# g.获取id = 1
# 的专题课，并打印该课程相关的课程大纲
#
# h.获取id = 1
# 的专题课，并打印该课程相关的所有章节
#
# i.获取id = 1
# 的专题课，并打印该课程相关的所有课时
# 第1章·Python
# 介绍、基础语法、流程控制
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 第1章·Python
# 介绍、基础语法、流程控制
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# i.获取id = 1
# 的专题课，并打印该课程相关的所有的价格策略
#



# 二、基于django
# rest
# framework
# 写路飞的接口（作业一 + rest
# framework
# 序列化）
# - 课程列表API
# - 课程详细API
