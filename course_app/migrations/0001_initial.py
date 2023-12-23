# Generated by Django 4.2.7 on 2023-11-30 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maruza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('fan', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=255)),
                ('maruza_fayl', models.FileField(upload_to='maruzalar')),
            ],
        ),
        migrations.CreateModel(
            name='Slayd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slaydlar')),
                ('title', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=255)),
                ('slayd_fayl', models.FileField(upload_to='slaydlar')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_id', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
