from django.contrib import admin
from . import models


# Register your models here.
# admin.site.register(models.Article)
# 上面是最初始的注册方式
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'content', 'date_time')
    list_filter = ('date_time',)


admin.site.register(models.Article, ArticleAdmin)
