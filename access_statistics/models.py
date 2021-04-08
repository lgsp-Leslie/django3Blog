from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.fields import exceptions
from django.utils import timezone


class ReadNum(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, verbose_name='统计模块')
    object_id = models.PositiveIntegerField('内容ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    read_num = models.IntegerField('阅读数', default=0)

    class Meta:
        verbose_name = '访问统计'
        verbose_name_plural = '访问统计'
        ordering = ['-read_num']


class ReadNumExpandMethod:
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            rn = ReadNum.objects.get(content_type=ct, object_id=self.id)
            return rn.read_num
        except exceptions.ObjectDoesNotExist:
            return 0


class ReadDetail(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, verbose_name='统计模块')
    object_id = models.PositiveIntegerField('内容ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    read_num = models.IntegerField('阅读数', default=0)
    date = models.DateField('日期', default=timezone.now)

    class Meta:
        verbose_name = '访问统计详情'
        verbose_name_plural = '访问统计详情'
