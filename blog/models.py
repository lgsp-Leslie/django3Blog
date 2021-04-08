from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models

from access_statistics.models import ReadNum
from access_statistics.models import ReadNumExpandMethod


class BlogType(models.Model):
    type_name = models.CharField('类型', max_length=30)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = '文章类型'


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField('标题', max_length=64)
    content = RichTextUploadingField('内容')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, verbose_name='博客类型')

    """
    def get_read_num(self):
        try:
            return self.readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0
    get_read_num.short_description = '阅读数'
    """

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_time']


"""
class ReadNum(models.Model):
    read_num = models.IntegerField('阅读数', default=0)
    blog = OneToOneField(Blog, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = '阅读数'
        verbose_name_plural = '阅读数'
        ordering = ['-read_num']
"""
