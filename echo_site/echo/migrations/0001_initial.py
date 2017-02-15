# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_name', models.CharField(max_length=255, verbose_name='\u8282\u70b9\u540d\u79f0')),
                ('node_type', models.CharField(choices=[('\u57fa\u5c42\u6cd5\u9662', '\u57fa\u5c42\u6cd5\u9662'), ('\u4e2d\u7ea7\u6cd5\u9662', '\u4e2d\u7ea7\u6cd5\u9662'), ('\u9ad8\u7ea7\u6cd5\u9662', '\u9ad8\u7ea7\u6cd5\u9662')], max_length=100, verbose_name='\u8282\u70b9\u7c7b\u578b')),
                ('node_address', models.CharField(max_length=255, verbose_name='\u8282\u70b9\u5730\u5740')),
                ('node_contact', models.CharField(blank=True, max_length=255, verbose_name='\u8282\u70b9\u8054\u7cfb\u4eba')),
                ('node_signer', models.CharField(default='system', max_length=50, verbose_name='\u767b\u8bb0\u4eba')),
                ('node_remarks', models.CharField(blank=True, max_length=255, verbose_name='\u5907\u6ce8')),
                ('node_signtime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]