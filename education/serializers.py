from rest_framework.serializers import ModelSerializer

from education.models import Course, Lesson


# Сериализатор курса
class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
