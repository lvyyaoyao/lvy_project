from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from api.utils.response import BaseResponse
from api import models
from rest_framework.viewsets import ViewSetMixin
from api.serializers.course import CourseSerializer, DegreeCourseListSerializer, DegreeCourseInfoSerializer, CourseModelSerializer, CourseQuestionSerializer
from api.serializers.course import CourseOutlineSerializer, CourseSectionSerializer

# c. 展示所有的专题课
# c_obj=Course.objects.filter(degree_course__isnull=True)

#
# class CoursesView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         ret = BaseResponse()
#         try:
#             # 从数据库获取数据
#             queryset = models.Course.objects.all()
#
#             # 分页
#             # page = PageNumberPagination()
#             # couesr_list = page.paginate_queryset(queryset, request, self)
#
#             # 分页后的结果执行序列化
#             ser = CourseSerializer(instance=queryset, many=True)
#             ret.data = ser.data
#             print(ret.data)
#         except Exception as e:
#             ret.code = 500
#             ret.error = '数据获取失败'
#         return Response(ret.dict)
#
#
# # a.查看所有学位课并打印学位课名称以及授课老师
#     # ret = models.DegreeCourse.objects.all().values('name', 'teachers__name')
# class DegreeCourseList(APIView):
#
#    def get(self, request, *args, **kwargs):
#         ret = BaseResponse()
#         try:
#             queryset = models.DegreeCourse.objects.all()
#             ser = DegreeCourseListSerializer(instance=queryset, many=True)
#             ret.data = ser.data
#         except Exception as e:
#             ret.code = 500
#             ret.error = '获取数据失败'
#         return Response(ret.dict)
#
#
# # b.查看所有学位课并打印学位课名称以及学位课的奖学金
#     # ret_obj = models.DegreeCourse.objects.all()
#     # for row in ret_obj:
#     #     print(row.name)
#     #     scholarships = row.scholarship_set.all()
#     #     for i in scholarships:
#     #         print(i.time_percent, i.value)
# class DegreeCourseInfo(APIView):
#
#     def get(self, request, *args, **kwargs):
#         ret = BaseResponse()
#         try:
#             ret_obj = models.DegreeCourse.objects.all()
#             ser = DegreeCourseInfoSerializer(instance=ret_obj)
#             ret.data = ser.data
#         except Exception as e:
#             ret.code = 500
#             ret.error = '获取数据失败'
#         return Response(ret.dict)
#
#
# # d. 查看id=1的学位课对应的所有模块名称
# # a_obj = DegreeCourse.objects.filter(id=1).values
#
# class CourseModel(APIView):
#     def get(self, request, *args, **kwargs):
#         ret = BaseResponse()
#         try:
#             queryset = models.Course.objects.filter(degree_course_id='1')
#             ser = CourseModelSerializer(instance=queryset)
#             ret.data = ser.data
#         except Exception as e:
#             ret.code = 500
#             ret.error = '获取数据失败'
#         return Response(ret.dict)
#
#
# # 获取id = 1的专题课，并打印该课程相关的所有常见问题
# class CourseQuestion(APIView):
#     def get(self, request, *args, **kwargs):
#         ret = BaseResponse()
#         try:
#             queryset = models.Course.objects.filter(id=1).first()
#             ser = CourseQuestionSerializer(instance=queryset)
#             ret.data = ser.data
#         except Exception as e:
#             ret.code = 500
#             ret.error = '获取数据失败'
#         return Response(ret.dict)
#
#
# # 获取id = 1的专题课，并打印该课程相关的课程大纲
# class CourseOutline(APIView):
#     def get(self, request, *args, **kwargs):
#         ret = BaseResponse()
#         try:
#             queryset = models.Course.objects.filter(id=1).first()
#             ser = CourseOutlineSerializer(instance=queryset)
#             ret.data = ser.data
#         except Exception as e:
#             ret.code = 500
#             ret.error = '获取数据失败'
#         return Response(ret.dict)
#
#
# # 获取id = 1的专题课，并打印该课程相关的所有章节
# class CourseSection(APIView):
#     def get(self, request, *args, **kwargs):
#         ret = BaseResponse()
#         try:
#             queryset = models.Course.objects.filter(id=1).first()
#             ser = CourseSectionSerializer(instance=queryset)
#             ret.data = ser.data
#         except Exception as e:
#             ret.code = 500
#             ret.error = '获取数据失败'
#         return Response(ret.dict)


class CoursesView(ViewSetMixin, APIView):

    def list(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            # 从数据库获取数据
            queryset = models.Course.objects.all()

            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)

            # 分页之后的结果执行序列化
            ser = CourseModelSerializer(instance=course_list,many=True)

            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)

    def retrieve(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.get(id=pk)
            ser = CourseModelSerializer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)
