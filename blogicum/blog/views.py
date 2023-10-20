from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from blog.models import Category, Post

from blog.const import INDEX_LIMIT


class PostFilter:
    """Фильтрует QuerySet."""

    def __init__(self, manager):
        self.manager = manager
        self.filter_criteries = {
            'is_published': True,
            'pub_date__lte': now(),
            'category__is_published': True
        }

    def by_category(self, category_slug):
        self.filter_criteries['category__slug'] = category_slug
        return self

    def get_queryset(self):
        return self.manager.filter(
            **self.filter_criteries
        ).select_related('author', 'location', 'category')


def index(request):
    post_list = PostFilter(Post.objects).get_queryset()[:INDEX_LIMIT]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        PostFilter(Post.objects).get_queryset(),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects,
        slug=category_slug,
        is_published=True
    )
    post_list = PostFilter(Post.objects).by_category(
        category_slug).get_queryset()
    return render(request, 'blog/category.html', {'category': category,
                                                  'post_list': post_list})
