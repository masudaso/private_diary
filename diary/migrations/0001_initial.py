# Generated by Django 5.1.1 on 2024-09-30 12:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('photo1', models.TextField(blank=True, null=True, verbose_name='写真1')),
                ('photo2', models.TextField(blank=True, null=True, verbose_name='写真2')),
                ('photo3', models.TextField(blank=True, null=True, verbose_name='写真3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='更新日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Diary',
            },
        ),
    ]
