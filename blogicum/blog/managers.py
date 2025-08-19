from django.db import models
from django.utils import timezone


class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            pub_date__lte=timezone.now(),
            category__is_published=True,
            is_published=True
        )
