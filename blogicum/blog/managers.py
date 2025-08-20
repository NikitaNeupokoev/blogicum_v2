from django.db import models
from django.utils import timezone


class PublishedPostManager(models.Manager):
    """
    Менеджер для получения опубликованных постов.

    Фильтрует посты по дате публикации,
    категории и статусу публикации.
    """

    def get_queryset(self):
        """
        Возвращает опубликованные посты
        с учетом даты и категории.
        """
        return super().get_queryset().filter(
            pub_date__lte=timezone.now(),
            category__is_published=True,
            is_published=True
        )
