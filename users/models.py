from django.db import models
from django.contrib.auth.models import AbstractUser

from src.constants import NULLABLE


# Класс модели пользователя
class User(AbstractUser):
    # Удаление имени пользователя, так как используем email в качестве уникального идентификатора
    username = None
    # Поле почты пользователя
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    # Поле телефона пользователя
    phone = models.CharField(
        max_length=50,
        verbose_name="Телефон",
        help_text="Укажите номер телефона",
        **NULLABLE
    )
    # Поле города пользователя
    city = models.CharField(max_length=35, verbose_name="Город", **NULLABLE)
    # Поле для хранения аватара пользователя
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите свой аватар",
        **NULLABLE
    )
    # email пользователя является полем входа в систему
    USERNAME_FIELD = "email"
    # Поля, которые должны заполняться при создании пользователя
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
