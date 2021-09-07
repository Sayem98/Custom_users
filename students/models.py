from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}'


class Student(models.Model):
    roll = models.IntegerField(unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return f'{self.user}'


class Teacher(models.Model):
    teacher_id = models.IntegerField(unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher')


class Results(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='result')
    cgpa = models.IntegerField()

    def __str__(self):
        return f'{self.student}'
