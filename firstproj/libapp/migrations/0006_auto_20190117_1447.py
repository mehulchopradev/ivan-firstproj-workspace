# Generated by Django 2.1.5 on 2019-01-17 09:17

from django.db import migrations, models
import libapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0005_auto_20190117_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to=libapp.models.buildprofilepicpath),
        ),
    ]
