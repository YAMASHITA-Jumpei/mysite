# Generated by Django 4.2.1 on 2023-06-07 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='タイトル')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='サブタイトル')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('introduction', models.TextField(verbose_name='自己紹介')),
                ('github', models.CharField(blank=True, max_length=100, null=True, verbose_name='github')),
                ('twitter', models.CharField(blank=True, max_length=100, null=True, verbose_name='twitter')),
                ('topimage', models.ImageField(upload_to='images', verbose_name='トップ画像')),
                ('subimage', models.ImageField(upload_to='images', verbose_name='サブ画像')),
            ],
        ),
    ]