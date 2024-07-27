from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.viewsets import ModelViewSet

from education.models import Course, Lesson, Payment
from education.serializers import CourseSerializer, LessonSerializer, PaymentSerializer
from users.models import ModeratorPermissions, IsOwner


# ViewSet для модели Курса
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [ModeratorPermissions | IsOwner]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# API для создания урока
class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [~ModeratorPermissions]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# API для получения списка уроков
class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [ModeratorPermissions | IsOwner]


# API для получения конкретного урока
class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [ModeratorPermissions | IsOwner]


# API для обновления урока
class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [ModeratorPermissions | IsOwner]


# API для удаления урока
class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [~ModeratorPermissions]


# API для получения списка платежей
class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer()
    queryset = Payment.objects.all()
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["payment_date"]
    filterset_fields = ["course", "lesson", "payment_method"]
    permission_classes = [ModeratorPermissions | IsOwner]
