from django.contrib import admin

from .models import Category, Location, Post


# Данные админки.
# 123
# 123@123.ru
# 123321qqq


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Location)
