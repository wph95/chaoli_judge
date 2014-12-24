# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe5\x90\x8d')),
                ('tag_type', models.IntegerField(verbose_name='\u6807\u7b7e\u7c7b\u578b', choices=[(1, '\u5b66\u79d1')])),
                ('description', models.CharField(max_length=255, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('order', models.IntegerField(default=0)),
                ('is_type', models.BooleanField(default=False)),
                ('parent_tag', models.ForeignKey(verbose_name='\u7236\u6807\u7b7e', blank=True, to='tags.Tag', null=True)),
            ],
            options={
                'ordering': ('tag_type', 'order', 'name'),
            },
            bases=(models.Model,),
        ),
    ]
