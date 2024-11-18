# Generated by Django 5.1.3 on 2024-11-18 08:12

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
            name='Tales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(help_text='Укажите тему сказки.', max_length=255, verbose_name='Тема сказки')),
                ('text', models.TextField(blank=True, default='текст', help_text='Введите текст сказки, который хотите добавить.', null=True, verbose_name='Текст сказки')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания записи.', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Дата и время последнего обновления записи.', verbose_name='Дата последнего обновления')),
                ('user', models.ForeignKey(blank=True, help_text='Пользователь, создавший сказку.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сказка',
                'verbose_name_plural': 'Сказки',
                'db_table': 'tales',
            },
        ),
        migrations.CreateModel(
            name='TopTales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(help_text='Укажите тему сказки.', max_length=255, verbose_name='Тема сказки')),
                ('text', models.TextField(blank=True, default='текст', help_text='Введите текст сказки, который хотите добавить.', null=True, verbose_name='Текст сказки')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания записи.', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Дата и время последнего обновления записи.', verbose_name='Дата последнего обновления')),
                ('user', models.ForeignKey(blank=True, help_text='Пользователь, создавший сказку.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Топ Сказка',
                'verbose_name_plural': 'Топ Сказки',
                'db_table': 'top_tales',
            },
        ),
    ]
