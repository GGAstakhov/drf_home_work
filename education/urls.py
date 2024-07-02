from django.urls import path
from rest_framework.routers import SimpleRouter

from education.apps import EducationConfig
from education.views import (CourseViewSet, LessonCreateAPIView,
                             LessonDestroyAPIView, LessonListAPIView,
                             LessonRetrieveAPIView, LessonUpdateAPIView,
                             PaymentListAPIView)

# Получаем имя приложения
app_name = EducationConfig.name

# Создание роутера
router = SimpleRouter()
router.register("", CourseViewSet)

# Создание списка url-шаблонов
urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_get"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path(
        "lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
    path(
        "lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
    path("payments/", PaymentListAPIView.as_view(), name="payment_list"),
]

# Объединение
urlpatterns += router.urls
