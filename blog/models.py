from django.contrib.auth.models import User
from django.db import models


class BlogType(models.Model):
    type_name = models.CharField('类型', max_length=30)

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = '文章类型'

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField('标题', max_length=64)
    content = models.TextField('内容')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title




