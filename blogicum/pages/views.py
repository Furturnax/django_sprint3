from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def about(request: HttpRequest) -> HttpResponse:
    """Рендерит страницу about.html с информацией о проекте."""
    return render(request, 'pages/about.html')


def rules(request: HttpRequest) -> HttpResponse:
    """Рендерит страницу rules.html с информацией о правилах."""
    return render(request, 'pages/rules.html')
