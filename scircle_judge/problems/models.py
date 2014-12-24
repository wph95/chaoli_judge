# coding: utf-8
import datetime

from django.db import models
from django.conf import settings

from tags.models import Tag

PROBLEM_STATUS = (
    (0, u'审核失败'),
    (1, u'审核通过'),
    (2, u'等待审核'),
    (3, u'已删除'),
)

LEVEL_CHOICES = (
    (0, u'未定级'),
    (1, u'简单'),
    (2, u'一般'),
    (3, u'较难'),
    (4, u'非常难'),
)


class Problem(models.Model):
    status = models.IntegerField('审核状态', choices=PROBLEM_STATUS)
    # basic information
    level = models.IntegerField('难度等级', choices=LEVEL_CHOICES, default=3)
    description = models.TextField('题目描述')
    option = models.TextField('选项')
    answer = models.IntegerField('答案')
    # submit status
    submit_count = models.PositiveIntegerField('提交次数', default=0)
    accept_count = models.PositiveIntegerField('通过次数', default=0)
    # filter information
    tags = models.ManyToManyField(Tag, verbose_name=u'标签', blank=True)
    # Author information
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='上传者', blank=True, null=True)
    last_modify = models.DateTimeField('最后修改', auto_now=True)

    class Meta:
        ordering = ('id', )
