# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngnts', '0004_bizservice_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u5e94\u7528\u7cfb\u7edf\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u5e94\u7528\u7cfb\u7edf',
                'verbose_name_plural': '\u5e94\u7528\u7cfb\u7edf',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AppService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u5e94\u7528\u670d\u52a1\u540d\u79f0')),
                ('app', models.ForeignKey(to='ngnts.Application')),
            ],
            options={
                'verbose_name': '\u5e94\u7528\u670d\u52a1',
                'verbose_name_plural': '\u5e94\u7528\u670d\u52a1',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='bizservice',
            name='dependencies',
            field=models.ManyToManyField(related_name='dependencies_rel_+', null=True, to='ngnts.BizService', blank=True),
            preserve_default=True,
        ),
    ]
