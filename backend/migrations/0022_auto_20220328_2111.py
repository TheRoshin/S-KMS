# Generated by Django 3.2.3 on 2022-03-29 01:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_alter_comment_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='postqus',
            name='view',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 28, 21, 11, 21, 99200), verbose_name='Commented on'),
        ),
    ]