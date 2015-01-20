# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngnts', '0002_bizcategory_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='BizService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u670d\u52a1\u540d\u79f0')),
                ('dependencies', models.ManyToManyField(related_name='dependencies_rel_+', to='ngnts.BizService')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u670d\u52a1',
                'verbose_name_plural': '\u4e1a\u52a1\u670d\u52a1',
            },
            bases=(models.Model,),
        ),
    ]
