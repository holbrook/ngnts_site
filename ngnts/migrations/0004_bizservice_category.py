# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngnts', '0003_bizservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='bizservice',
            name='category',
            field=models.ForeignKey(default=1, to='ngnts.BizCategory'),
            preserve_default=False,
        ),
    ]
