from django import forms
from .models import User, Teacher
from django.contrib.auth.forms import UserCreationForm
from .models import Student


def get_student_choices():
    all_students = Student.objects.all()
    list_choices = []

    for student in all_students:
        list_choices.append((student, student))
    print(list_choices)
    choices = tuple(list_choices)

    return choices


class StudentSingUpForm(UserCreationForm):
    roll = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'roll']


class TeacherSingUpForm(UserCreationForm):
    teacher_id = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'teacher_id']


class AddResultForm(forms.Form):
    cgpa = forms.IntegerField()
    student = forms.ChoiceField(choices=get_student_choices())


class ViewResult(forms.Form):
    roll = forms.IntegerField()
