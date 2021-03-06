# Generated by Django 2.1.5 on 2019-01-16 10:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0002_auto_20190108_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pages', models.IntegerField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('published', models.DateField(default=datetime.date(2019, 1, 16), null=True)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ratings', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libapp.Book')),
            ],
        ),
        migrations.CreateModel(
            name='UserBookIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuedate', models.DateField(default=datetime.date(2019, 1, 16))),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libapp.Book')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(choices=[('IN', 'India'), ('NE', 'Netherlands')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1),
        ),
        migrations.AddField(
            model_name='userbookissue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libapp.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='publicationhouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libapp.PublicationHouse'),
        ),
        migrations.AddField(
            model_name='user',
            name='booksissued',
            field=models.ManyToManyField(through='libapp.UserBookIssue', to='libapp.Book'),
        ),
    ]
