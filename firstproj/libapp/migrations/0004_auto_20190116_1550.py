# Generated by Django 2.1.5 on 2019-01-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0003_auto_20190116_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookissue',
            name='issuedate',
            field=models.DateField(),
        ),
    ]
