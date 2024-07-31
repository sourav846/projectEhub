# Generated by Django 5.0.4 on 2024-07-29 04:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Description', models.CharField(blank=True, max_length=1000, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Rate', models.FloatField(max_length=11)),
                ('Uuid', models.UUIDField(default=uuid.uuid4)),
                ('File', models.FileField(upload_to='video')),
                ('Image', models.ImageField(upload_to='img')),
                ('Poster', models.ImageField(upload_to='poster')),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
    ]