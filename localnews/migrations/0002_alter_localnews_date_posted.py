# Generated by Django 4.0.5 on 2022-08-02 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localnews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localnews',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 2, 10, 26, 55, 395390)),
        ),
    ]
