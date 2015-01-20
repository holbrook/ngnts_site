# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngnts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bizcategory',
            name='parent',
            field=models.ForeignKey(related_name='children', blank=True, to='ngnts.BizCategory', null=True),
            preserve_default=True,
        ),
    ]
