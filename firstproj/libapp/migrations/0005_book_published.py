# Generated by Django 2.1.5 on 2019-01-10 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateField(default=datetime.date(2019, 1, 10), null=True),
        ),
    ]
