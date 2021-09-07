# Generated by Django 3.2.5 on 2021-09-05 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_student_roll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgpa', models.IntegerField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='students.student')),
            ],
        ),
    ]