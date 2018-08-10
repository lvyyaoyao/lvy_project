from django.shortcuts import render,HttpResponse
from api import models


def index(request):
    # a.查看所有学位课并打印学位课名称以及授课老师
    # ret = models.DegreeCourse.objects.all().values('name', 'teachers__name')

    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    # ret_obj = models.DegreeCourse.objects.all()
    # for row in ret_obj:
    #     print(row.name)
    #     scholarships = row.scholarship_set.all()
    #     for i in scholarships:
    #         print(i.time_percent, i.value)

    # c.展示所有的专题课
    # ret = models.Course.objects.filter(degree_course__isnull=True)

    # d.查看id = 1
    # 的学位课对应的所有模块名称
    # ret = models.Course.objects.filter(degree_course_id='1')

    # e.获取id = 1
    # 的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    # ret = models.Course.objects.filter(id='1')
    # print(ret.values('name'))
    # print(ret.values('brief'))
    # print(ret.first().get_level_display())

    # filter和get区别在于得出的数据类型不一样，所以取值方法也不一样！！！！！
    # ret = models.Course.objects.get(id='1')
    # print(ret.coursedetail.hours)
    # print(ret.coursedetail.why_study)
    # print(ret.coursedetail.recommend_courses.all())

    # f.获取id = 1
    # 的专题课，并打印该课程相关的所有常见问题
    # ret = models.OftenAskedQuestion.objects.filter(object_id='1', content_type__model='course')

    # g.获取id = 1
    # 的专题课，并打印该课程相关的课程大纲
    # ret = models.Course.objects.filter(id='1').values('coursedetail__courseoutline__title')

    # h.获取id = 1
    # 的专题课，并打印该课程相关的所有章节
    # ret = models.Course.objects.filter(id='1').values('coursechapters__chapter', 'coursechapters__name')

    # i.获取id = 1
    # 的专题课，并打印该课程相关的所有课时
    # ret = models.Course.objects.filter(id='1').values('coursechapters__coursesections__name', 'coursechapters__coursesections__order')

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
    # ret = models.PricePolicy.objects.filter(object_id='1', content_type__model='course')

    # print(ret)
    return HttpResponse('ok')

    # 二、基于django
    # rest
    # framework
    # 写路飞的接口（作业一 + rest
    # framework
    # 序列化）
    # - 课程列表API
    # - 课程详细API