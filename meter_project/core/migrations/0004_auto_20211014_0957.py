# Generated by Django 3.2.7 on 2021-10-14 09:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211014_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='device',
            name='full_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='device',
            name='part_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='device',
            name='part_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='meter',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='meter',
            name='full_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='meter',
            name='part_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='meter',
            name='part_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), blank=True, default=list, size=None),
        ),
    ]
