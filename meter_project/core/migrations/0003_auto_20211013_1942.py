# Generated by Django 3.2.7 on 2021-10-13 19:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211013_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='full_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='part_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='part_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='city',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='city',
            name='full_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='city',
            name='part_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='city',
            name='part_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='district',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='district',
            name='full_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='district',
            name='part_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='district',
            name='part_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='house',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='house',
            name='full_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='house',
            name='part_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='house',
            name='part_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='street',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='street',
            name='full_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='street',
            name='part_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='street',
            name='part_owner_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=None),
        ),
    ]
