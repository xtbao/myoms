# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20161214_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u7ec4\u4fe1\u606f',
                'verbose_name_plural': '\u4e3b\u673a\u7ec4\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idc_name', models.CharField(max_length=40, verbose_name=b'\xe6\x9c\xba\xe6\x88\xbf\xe5\x90\x8d\xe7\xa7\xb0')),
                ('remark', models.CharField(max_length=40, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
            options={
                'verbose_name': '\u673a\u623f\u5217\u8868',
                'verbose_name_plural': '\u673a\u623f\u5217\u8868',
            },
        ),
        migrations.AlterModelOptions(
            name='hostlist',
            options={'verbose_name': '\u4e3b\u673a\u5217\u8868', 'verbose_name_plural': '\u4e3b\u673a\u5217\u8868'},
        ),
        migrations.RemoveField(
            model_name='hostlist',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='hostlist',
            name='status',
        ),
        migrations.AddField(
            model_name='hostlist',
            name='bianhao',
            field=models.CharField(default=1, max_length=30, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostlist',
            name='idc_name',
            field=models.CharField(max_length=40, null=True, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x88\xbf', blank=True),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='hostname',
            field=models.CharField(max_length=30, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='ip',
            field=models.GenericIPAddressField(unique=True, verbose_name=b'IP\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AddField(
            model_name='hostlist',
            name='group',
            field=models.ManyToManyField(to='asset.Group', verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d', blank=True),
        ),
    ]
