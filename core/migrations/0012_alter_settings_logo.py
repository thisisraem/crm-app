# Generated by Django 4.1.7 on 2023-07-30 08:20

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_delete_customergenderchart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/settings', validators=[core.models.validate_png_image]),
        ),
    ]
