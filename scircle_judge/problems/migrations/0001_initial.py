# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(verbose_name=b'\xe5\xae\xa1\xe6\xa0\xb8\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, '\u5ba1\u6838\u5931\u8d25'), (1, '\u5ba1\u6838\u901a\u8fc7'), (2, '\u7b49\u5f85\u5ba1\u6838'), (3, '\u5df2\u5220\u9664')])),
                ('level', models.IntegerField(default=3, verbose_name=b'\xe9\x9a\xbe\xe5\xba\xa6\xe7\xad\x89\xe7\xba\xa7', choices=[(0, '\u672a\u5b9a\u7ea7'), (1, '\u7b80\u5355'), (2, '\u4e00\u822c'), (3, '\u8f83\u96be'), (4, '\u975e\u5e38\u96be')])),
                ('description', models.TextField(verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('option', models.TextField(verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9')),
                ('answer', models.IntegerField(verbose_name=b'\xe7\xad\x94\xe6\xa1\x88')),
                ('submit_count', models.PositiveIntegerField(default=0, verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\xac\xa1\xe6\x95\xb0')),
                ('accept_count', models.PositiveIntegerField(default=0, verbose_name=b'\xe9\x80\x9a\xe8\xbf\x87\xe6\xac\xa1\xe6\x95\xb0')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9')),
                ('data_timestamp', models.DateTimeField(null=True, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3', blank=True)),
                ('author', models.ForeignKey(verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe8\x80\x85', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tags', models.ManyToManyField(to='tags.Tag', verbose_name='\u6807\u7b7e', blank=True)),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
    ]
