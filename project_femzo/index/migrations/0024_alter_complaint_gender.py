# Generated by Django 3.2.7 on 2021-12-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0023_complaint_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='gender',
            field=models.CharField(default='NA', max_length=50),
        ),
    ]
