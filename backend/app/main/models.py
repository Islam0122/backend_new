from django.db import models


# Create your models here.
DIRECTION_CHOICES = [
        ('FRONTEND', 'Фронтенд'),
        ('BACKEND', 'Бекенд'),
    ]


class Group(models.Model):
    group_name = models.CharField("Название группы", max_length=100)
    group_description = models.TextField("Описание группы")
    direction = models.CharField("Направление", max_length=10, choices=DIRECTION_CHOICES)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.group_name


class Student(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    age = models.IntegerField("Возраст")
    phone_number = models.CharField("Телефонный номер", max_length=15, unique=True)
    telegram = models.CharField("Telegram", max_length=100, unique=True)
    photo = models.ImageField("Фото", upload_to="students/photos/", null=True, blank=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
