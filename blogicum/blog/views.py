from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from blog.const import INDEX_LIMIT
from blog.models import Category, Post


def filter_posts(query_set):
    """Фильтрует посты по определенным критериям."""
    return query_set.filter(
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True,
    ).select_related('author', 'location', 'category',)


def index(request: HttpRequest) -> HttpResponse:
    """Рендерит страницу index.html с постами."""
    post_list = filter_posts(Post.objects)[:INDEX_LIMIT]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    """Рендерит страницу detail.html с данными конкретного поста."""
    post = get_object_or_404(filter_posts(Post.objects), pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    """Рендерит страницу category.html с постами определённой категории."""
    category = get_object_or_404(
        Category.objects,
        slug=category_slug,
        is_published=True
    )
    post_list = filter_posts(category.posts.all())
    return render(request, 'blog/category.html', {'category': category,
                                                  'post_list': post_list})
