from rest_framework import serializers
from api import models


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class DegreeCourseListSerializer(serializers.Serializer):
    name = serializers.CharField()
    teachers = serializers.SerializerMethodField()
    class Meta:
        model = models.DegreeCourse
        # fields = ['id','name','level_name','hours','course_slogan','recommend_courses']
        fields = ['name', 'teachers']

    def get_teachers(self, row):
        teachers_list = row.teachers.all()
        return [{'name': item.name} for item in teachers_list]


class DegreeCourseInfoSerializer(serializers.Serializer):
    course = serializers.SerializerMethodField()

    def get_values(self, row):
        scholarship_list = row.scholarship_set.all()
        return [item.value for item in scholarship_list]

    class Meta:
        model = models.DegreeCourse
        fields = ['name', 'course']


class CourseModelSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ["name"]


class CourseQuestionSerializer(serializers.Serializer):
    ask = serializers.SerializerMethodField()

    def get_ask(self,obj):
        ask_list = obj.asked_question.all()
        return [(item.question, item.answer) for item in ask_list]

    class Meta:
        model = models.Course
        fields = ["ask"]


class CourseOutlineSerializer(serializers.Serializer):
    outline = serializers.SerializerMethodField()

    def get_outline(self, obj):
        outline_list = obj.coursedetail.courseoutline_set.all()
        return [(item.title, item.content) for item in outline_list]

    class Meta:
        model = models.Course
        fields = ["outline"]


class CourseSectionSerializer(serializers.Serializer):
    chapter = serializers.CharField(source="coursechapters.name")

    class Meta:
        model = models.Course
        fields = ["chapter"]
