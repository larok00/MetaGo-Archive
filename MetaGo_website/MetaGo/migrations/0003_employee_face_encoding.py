# Generated by Django 2.1 on 2018-08-09 13:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetaGo', '0002_auto_20180809_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='face_encoding',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, null=True, size=128),
        ),
    ]
