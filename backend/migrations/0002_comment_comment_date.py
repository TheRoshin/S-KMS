# Generated by Django 3.2.3 on 2022-02-07 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 17, 49, 19, 903624), verbose_name='Commented on'),
        ),
    ]