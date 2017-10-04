# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 10:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rating.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, unique=True)),
                ('cat_and_punct', models.IntegerField(validators=[rating.models.validate_ratingrange], verbose_name='Catering and Punctuality')),
                ('cleanliness', models.IntegerField(validators=[rating.models.validate_ratingrange], verbose_name='Cleanliness')),
                ('breakfast', models.IntegerField(validators=[rating.models.validate_ratingrange], verbose_name='Breakfast')),
                ('lunch', models.IntegerField(validators=[rating.models.validate_ratingrange], verbose_name='Lunch')),
                ('dinner', models.IntegerField(validators=[rating.models.validate_ratingrange], verbose_name='Dinner')),
                ('hostel', models.CharField(choices=[(b'Barak', b'Barak'), (b'Brahmaputra', b'Brahmaputra'), (b'Dhansiri', b'Dhansiri'), (b'Dibang', b'Dibang'), (b'Dihing', b'Dihing'), (b'Kameng', b'Kameng'), (b'Kapili', b'Kapili'), (b'Manas', b'Manas'), (b'Siang', b'Siang'), (b'Subansiri', b'Subansiri'), (b'Umiam', b'Umiam'), (b'Lohit', b'Lohit'), (b'Married Scholars', b'Married Scholars')], max_length=20)),
                ('meal', models.CharField(choices=[(b'Breakfast', b'Breakfast'), (b'Lunch', b'Lunch'), (b'Dinner', b'Dinner')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid', models.CharField(max_length=20, unique=True)),
                ('rollno', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('resident_hostel', models.CharField(choices=[(b'Barak', b'Barak'), (b'Brahmaputra', b'Brahmaputra'), (b'Dhansiri', b'Dhansiri'), (b'Dibang', b'Dibang'), (b'Dihing', b'Dihing'), (b'Kameng', b'Kameng'), (b'Kapili', b'Kapili'), (b'Manas', b'Manas'), (b'Siang', b'Siang'), (b'Subansiri', b'Subansiri'), (b'Umiam', b'Umiam'), (b'Lohit', b'Lohit'), (b'Married Scholars', b'Married Scholars')], max_length=20)),
                ('subscribed_hostel', models.CharField(choices=[(b'Barak', b'Barak'), (b'Brahmaputra', b'Brahmaputra'), (b'Dhansiri', b'Dhansiri'), (b'Dibang', b'Dibang'), (b'Dihing', b'Dihing'), (b'Kameng', b'Kameng'), (b'Kapili', b'Kapili'), (b'Manas', b'Manas'), (b'Siang', b'Siang'), (b'Subansiri', b'Subansiri'), (b'Umiam', b'Umiam'), (b'Lohit', b'Lohit'), (b'Married Scholars', b'Married Scholars')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
