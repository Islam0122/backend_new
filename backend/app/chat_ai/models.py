from django.db import models
from django.contrib.auth.models import User


class Base_Tales(models.Model):
    topic = models.CharField(
        max_length=255,
        verbose_name='Тема сказки',
        help_text='Укажите тему сказки.'
    )
    text = models.TextField(
        verbose_name='Текст сказки',
        help_text='Введите текст сказки, который хотите добавить.'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Пользователь, создавший сказку.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Дата и время создания записи.'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего обновления',
        help_text='Дата и время последнего обновления записи.'
    )

    class Meta:
        abstract = True


class Tales(Base_Tales):
    class Meta:
        db_table = 'tales'
        verbose_name = 'Сказка'
        verbose_name_plural = 'Сказки'


class TopTales(Base_Tales):
    class Meta:
        db_table = 'top_tales'
        verbose_name = 'Топ Сказка'
        verbose_name_plural = 'Топ Сказки'
