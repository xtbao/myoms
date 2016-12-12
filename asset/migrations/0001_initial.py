# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=20, verbose_name=b'IP\xe5\x9c\xb0\xe5\x9d\x80')),
                ('hostname', models.CharField(max_length=30, verbose_name=b'IP\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('product', models.CharField(max_length=20, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81')),
                ('application', models.CharField(max_length=20, verbose_name=b'\xe5\xba\x94\xe7\x94\xa8')),
                ('idc_jg', models.CharField(max_length=10, verbose_name=b'\xe6\x9c\xba\xe6\x9f\x9c\xe7\xbc\x96\xe5\x8f\xb7', blank=True)),
                ('status', models.CharField(max_length=10, verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe7\x8a\xb6\xe6\x80\x81')),
                ('remark', models.TextField(max_length=50, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u5217\u8868\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='ServerAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manufacturer', models.CharField(max_length=20, verbose_name=b'\xe5\x8e\x82\xe5\x95\x86')),
                ('service_sn', models.CharField(unique=True, max_length=80, verbose_name=b'\xe5\xba\x8f\xe5\x88\x97\xe5\x8f\xb7')),
                ('cpu_model', models.CharField(max_length=50, verbose_name=b'CPU\xe5\x9e\x8b\xe5\x8f\xb7')),
                ('cpu_nums', models.PositiveSmallIntegerField(verbose_name=b'CPU\xe7\xba\xbf\xe7\xa8\x8b\xe6\x95\xb0')),
                ('mem', models.CharField(max_length=5, verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('disk', models.CharField(max_length=5, verbose_name=b'\xe7\xa1\xac\xe7\x9b\x98\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('hostname', models.CharField(max_length=30, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('ip', models.CharField(max_length=20, verbose_name=b'IP\xe5\x9c\xb0\xe5\x9d\x80')),
                ('macaddress', models.CharField(max_length=40, verbose_name=b'MAC\xe5\x9c\xb0\xe5\x9d\x80')),
                ('os', models.CharField(max_length=20, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('virtual', models.CharField(max_length=20, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe8\x99\x9a\xe6\x8b\x9f\xe6\x9c\xba')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u8d44\u4ea7\u4fe1\u606f',
                'verbose_name_plural': '\u4e3b\u673a\u8d44\u4ea7\u4fe1\u606f\u7ba1\u7406',
            },
        ),
    ]
