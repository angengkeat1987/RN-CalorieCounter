# Generated by Django 3.0.6 on 2020-06-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DietManApp', '0002_auto_20200605_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditems',
            name='Name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='fooditems',
            name='Time',
            field=models.TimeField(default=''),
        ),
    ]
