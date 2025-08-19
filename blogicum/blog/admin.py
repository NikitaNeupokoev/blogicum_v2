from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """
    Админ-интерфейс для модели Location.

    Поля: id, name, created_at.
    Поиск по name, сортировка по имени.
    """

    list_display = (
        'id',
        'name',
        'created_at',
    )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Админ-интерфейс для модели Category.

    Поля: id, title, slug, created_at.
    Поиск по title и slug, слаг заполняется автоматически.
    Сортировка по title.
    """

    list_display = (
        'id',
        'title',
        'slug',
        'created_at',
    )
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Админ-интерфейс для модели Post.

    Поля: id, title, author, pub_date, location, category.
    Поиск по title, author (по имени пользователя) и text.
    Фильтрация по author, location, category, pub_date.
    Сортировка по дате публикации (по убыванию).
    """

    list_display = (
        'id',
        'title',
        'author',
        'pub_date',
        'location',
        'category'
    )
    search_fields = (
        'title',
        'author__username',
        'text'
    )
    list_filter = (
        'author',
        'location',
        'category',
        'pub_date'
    )
    ordering = ('-pub_date',)
