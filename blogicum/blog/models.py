from django.contrib.auth import get_user_model
from django.db import models

from .constants import (
    MAX_LENGTH_TITLE,
    MAX_SLICE_LENGTH_TITLE,
)
from core.models import BaseModel
from .managers import PublishedPostManager

User = get_user_model()


class Location(BaseModel):
    """
    Модель для представления местоположения.

    Атрибуты:
    - name: Название места (строка).
    """

    name = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        verbose_name='Название места'
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name[:MAX_SLICE_LENGTH_TITLE]


class Category(BaseModel):
    """
    Модель для представления категории поста.

    Атрибуты:
    - title: Заголовок категории (строка).
    - description: Описание категории (текст).
    - slug: Уникальный идентификатор для URL (строка).
    """

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; '
            'разрешены символы латиницы, цифры, дефис и подчёркивание.'
        )
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:MAX_SLICE_LENGTH_TITLE]


class Post(BaseModel):
    """
    Модель для представления поста.

    Атрибуты:
    - title: Заголовок поста (строка).
    - text: Текст поста (текст).
    - pub_date: Дата и время публикации (дата/время).
    - author: Автор публикации (внешний ключ на User).
    - location: Местоположение поста
      (внешний ключ на Location, может быть пустым).
    - category: Категория поста
      (внешний ключ на Category, может быть пустым).
    """

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        verbose_name='Заголовок'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем — '
            'можно делать отложенные публикации.'
        )
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория'
    )

    objects = models.Manager()
    published = PublishedPostManager()

    class Meta(BaseModel.Meta):
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.title[:MAX_SLICE_LENGTH_TITLE]} -'
        f'{self.author.username}'
