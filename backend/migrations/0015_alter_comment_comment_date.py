# Generated by Django 3.2.3 on 2022-03-09 22:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_auto_20220308_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 9, 17, 51, 3, 153097), verbose_name='Commented on'),
        ),
    ]
