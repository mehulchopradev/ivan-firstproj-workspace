# Generated by Django 2.1.5 on 2019-01-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0006_auto_20190114_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
