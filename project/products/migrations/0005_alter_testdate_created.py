# Generated by Django 5.2.3 on 2025-06-27 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_testdate_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdate',
            name='Created',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 27, 17, 18, 0, 184272)),
        ),
    ]
