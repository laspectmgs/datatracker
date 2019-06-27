# Copyright The IETF Trust 2018-2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 10:52


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('rsn', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'registrations',
            },
        ),
        migrations.CreateModel(
            name='InterimMeeting',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('meeting.meeting',),
        ),
    ]
