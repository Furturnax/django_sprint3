from django.shortcuts import render, redirect



def index(request):
    template = 'blog/index.html'
    context = {'posts': posts[::-1]}
    return render(request, template, context)


def post_detail(request, id):
    try:
        context = {'post': posts[id]}
    except IndexError:
        return redirect('blog:index')

    template = 'blog/detail.html'
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)
