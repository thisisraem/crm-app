# Generated by Django 4.2.1 on 2023-06-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_customerrecords_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrecords',
            name='age',
            field=models.CharField(choices=[('12-18', '12-18'), ('18-25', '18-25'), ('25-35', '25-35'), ('35-50', '35-50'), ('more-than-50', 'More than 50')], max_length=15),
        ),
    ]
