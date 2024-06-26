from rest_framework.serializers import ModelSerializer, SerializerMethodField

from education.models import Course, Lesson, Payment


# Сериализатор урока
class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('course', 'title', 'description', 'preview', 'video_url')


# Сериализатор курса
class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, source='lesson_set')

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ('name', 'description', 'image', 'lesson_count', 'lessons')


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ('user', 'payment_date', 'course', 'lesson', 'amount', 'payment_method')
