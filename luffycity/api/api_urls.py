from django.conf.urls import url
from api import views
from api.views import course
from api.views import ShoppingCarView


urlpatterns = [
    # url(r'courses/$', course.CoursesView.as_view()),
    # url(r'degree_course/$', course.DegreeCourseList.as_view()),
    # url(r'DegreeCourseInfo/$', course.DegreeCourseInfo.as_view()),   # 有问题
    # url(r'CourseModel/$', course.CourseModel.as_view()),            # 有问题
    # url(r'CourseQuestion/$', course.CourseQuestion.as_view()),
    # url(r'CourseOutline/$', course.CourseOutline.as_view()),
    # url(r'CourseSection/$', course.CourseSection.as_view()),
    # url(r'courses/$', course.CoursesView.as_view({'get': 'list'})),
    # url(r'courses/(?P<pk>\d+)/$', course.CoursesView.as_view({'get': 'retrieve'})),
    url(r'shoppingcar/$', ShoppingCarView.ShoppingCarView.as_view({'post': 'create', 'get': 'list', 'delete': 'destroy', 'put': 'update'})),
]