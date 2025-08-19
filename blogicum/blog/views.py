from django.shortcuts import render, get_object_or_404

from .models import Post, Category
from .constants import MAX_POSTS_PER_PAGE


def index(request):
    return render(
        request,
        'blog/index.html',
        {'post_list': Post.published.all()[:MAX_POSTS_PER_PAGE]}
    )


def post_detail(request, post_id):
    return render(
        request,
        'blog/detail.html',
        {'post': get_object_or_404(Post.published, id=post_id)}
    )


def category_posts(request, category_slug):
    return render(
        request,
        'blog/category.html',
        {
            'category': get_object_or_404(
                Category,
                slug=category_slug,
                is_published=True
            ),
            'post_list': get_object_or_404(
                Category,
                slug=category_slug,
                is_published=True).posts(manager='published').all()
        }
    )
