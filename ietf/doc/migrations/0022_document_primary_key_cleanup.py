# Copyright The IETF Trust 2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-10 03:47


from django.db import migrations, models
import django.db.models.deletion
import ietf.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0021_remove_docs2_m2m'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docalias',
            name='document',
            field=ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Document'),
        ),
        migrations.AlterField(
            model_name='docalias',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='docevent',
            name='doc',
            field=ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Document'),
        ),
        migrations.AlterField(
            model_name='dochistory',
            name='doc',
            field=ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_set', to='doc.Document'),
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='documentauthor',
            name='document',
            field=ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Document'),
        ),
        migrations.AlterField(
            model_name='documenturl',
            name='doc',
            field=ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Document'),
        ),
        migrations.AlterField(
            model_name='relateddochistory',
            name='target',
            field=ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reversely_related_document_history_set', to='doc.DocAlias'),
        ),
        migrations.AlterField(
            model_name='relateddocument',
            name='source',
            field=ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Document'),
        ),
        migrations.AlterField(
            model_name='relateddocument',
            name='target',
            field=ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.DocAlias'),
        ),
    ]
