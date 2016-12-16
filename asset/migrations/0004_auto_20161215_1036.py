# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20161215_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostlist',
            name='group',
            field=models.ManyToManyField(to='asset.Group', null=True, verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d', blank=True),
        ),
    ]
