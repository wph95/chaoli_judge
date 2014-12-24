# coding: utf-8
from django.db import models
from tags.constants import TAG_TYPE_CHOICES


class Tag(models.Model):
    name = models.CharField('标签名', max_length = 255, unique = True)
    tag_type = models.IntegerField(verbose_name=u'标签类型', choices=TAG_TYPE_CHOICES)
    description = models.CharField('描述', max_length = 255, blank = True)
    parent_tag = models.ForeignKey('Tag', verbose_name = u'父标签', blank = True, null = True)
    order = models.IntegerField(default = 0)
    is_type = models.BooleanField(default = False)
    
    
    def n_problems(self):
        return self.problem_set.filter(status = 1).count()
        
    class Meta:
        ordering = ('tag_type', 'order', 'name')
        
    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u'%s %s'%(self.tag_type, self.name)
