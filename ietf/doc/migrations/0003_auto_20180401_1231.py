# Copyright The IETF Trust 2018-2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-01 12:31


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0002_auto_20180220_1052'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='docevent',
            index=models.Index(fields=[b'type', b'doc'], name='doc_doceven_type_43e53e_idx'),
        ),
    ]
