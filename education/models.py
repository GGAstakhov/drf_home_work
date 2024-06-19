from django.db import models

from src.constants import NULLABLE


# Класс модели Курс
class Course(models.Model):
    # Поле названия курса
    name = models.CharField(
        max_length=150,
        verbose_name="Название Курса",
        help_text="Укажите название курса",
    )
    # Поле для хранения превью курса
    image = models.ImageField(
        upload_to="education/courses",
        verbose_name="Превью",
        help_text="Загрузите фото",
        **NULLABLE,
    )
    # Поле для хранения описания курса
    description = models.TextField(
        verbose_name="Описание курса", help_text="Опишите суть курса", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


# Класс модели Урок
class Lesson(models.Model):
    # Поле для связывания моделей Курса и Урока
    course = models.ForeignKey("Course", on_delete=models.CASCADE, verbose_name="курс")
    # Поле для хранения названия урока
    title = models.CharField(
        max_length=200, verbose_name="название", help_text="Укажите название урока"
    )
    # Поле для хранения описания урока
    description = models.TextField(
        verbose_name="описание", help_text="Опишите суть урока", **NULLABLE
    )
    # Поле для хранения превью урока
    preview = models.ImageField(
        upload_to="lesson",
        verbose_name="первью",
        help_text="Загрузите фото",
        **NULLABLE,
    )
    # Поле для хранения ссылки на видео урока
    video_url = models.URLField(**NULLABLE, verbose_name="видео")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
