# Generated by Django 4.2.7 on 2023-12-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0002_video_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amaliy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('fan', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=255)),
                ('amaliy_fayl', models.FileField(upload_to='amaliylar')),
            ],
            options={
                'verbose_name_plural': "Amaliy mashg'ulotlar",
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Testlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('fan', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=255)),
                ('test_fayl', models.FileField(upload_to='testlar')),
            ],
            options={
                'verbose_name_plural': 'testlar',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='maruza',
            options={'ordering': ['-id'], 'verbose_name_plural': "Ma'ruzalar"},
        ),
        migrations.AlterModelOptions(
            name='slayd',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Slaydlar'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Videolar'},
        ),
        migrations.AlterModelOptions(
            name='videocategory',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Video kategoriyalari'},
        ),
    ]
