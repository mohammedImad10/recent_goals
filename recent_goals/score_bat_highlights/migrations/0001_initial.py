# Generated by Django 5.1.3 on 2024-11-24 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatHighlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('competition', models.CharField(max_length=70)),
                ('date', models.DateField(default=datetime.date.today)),
                ('embed_video', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
