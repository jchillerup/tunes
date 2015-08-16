# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('description', models.TextField()),
                ('filesystem', models.FileField(upload_to='')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecordingAnnotation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('offset', models.IntegerField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('recording', models.ForeignKey(to='web.Recording')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('abc', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('last_modified', models.DateTimeField()),
                ('meter', models.CharField(max_length=255)),
                ('unit_note', models.CharField(max_length=10)),
                ('tempo', models.CharField(max_length=10)),
                ('key', models.CharField(max_length=10)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tune',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('origin', models.CharField(max_length=255)),
                ('composer', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=30)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TuneBook',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('public', models.BooleanField()),
                ('type', models.CharField(max_length=32, choices=[('personal', 'Personal tune book'), ('tunebook', 'Tune book'), ('teacher', 'Teacher'), ('setlist', 'Set list')])),
                ('tunes', models.ManyToManyField(to='web.Tune')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TuneComment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TuneRelation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('tune', models.ForeignKey(to='web.Tune')),
            ],
        ),
        migrations.AddField(
            model_name='setting',
            name='tune',
            field=models.ForeignKey(to='web.Tune'),
        ),
        migrations.AddField(
            model_name='recordingannotation',
            name='tune',
            field=models.ForeignKey(null=True, to='web.Tune'),
        ),
    ]
