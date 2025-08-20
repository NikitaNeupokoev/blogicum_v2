from django.db import models


class BaseModel(models.Model):
    """
    Абстрактная базовая модель для других моделей.

    Добавляет поля:
    - is_published: статус публикации.
    - created_at: дата создания записи.
    """

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']
