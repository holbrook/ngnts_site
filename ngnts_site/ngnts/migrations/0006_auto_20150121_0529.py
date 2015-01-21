# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngnts', '0005_auto_20150120_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='BizLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u540d\u79f0')),
                ('doc', models.TextField(null=True, verbose_name='\u8bf4\u660e', blank=True)),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u7ea7\u522b',
                'verbose_name_plural': '\u4e1a\u52a1\u7ea7\u522b',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bizcategory',
            name='level',
        ),
        migrations.RemoveField(
            model_name='bizcategory',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='bizcategory',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='bizcategory',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='bizcategory',
            name='tree_id',
        ),
        migrations.AddField(
            model_name='application',
            name='doc',
            field=models.TextField(null=True, verbose_name='\u8bf4\u660e', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appservice',
            name='doc',
            field=models.TextField(null=True, verbose_name='\u8bf4\u660e', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bizcategory',
            name='doc',
            field=models.TextField(null=True, verbose_name='\u8bf4\u660e', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bizservice',
            name='doc',
            field=models.TextField(null=True, verbose_name='\u8bf4\u660e', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bizservice',
            name='level',
            field=models.ForeignKey(blank=True, to='ngnts.BizLevel', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bizservice',
            name='category',
            field=models.ForeignKey(blank=True, to='ngnts.BizCategory', null=True),
            preserve_default=True,
        ),
    ]
