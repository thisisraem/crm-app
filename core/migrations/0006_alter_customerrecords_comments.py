# Generated by Django 4.2.1 on 2023-06-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_customerrecords_is_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrecords',
            name='comments',
            field=models.TextField(blank=True, max_length=1600, null=True),
        ),
    ]
