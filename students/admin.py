from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, Teacher, Results
from .forms import StudentSingUpForm


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['roll', 'user']


class ResultsAdmin(admin.ModelAdmin):
    model = Results
    list_display = ['cgpa', 'student']


class TeacherAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['teacher_id', 'user']


class CustomUserAdmin(UserAdmin):
    add_form = StudentSingUpForm
    model = User
    list_display = ['email', 'username', 'is_student', 'is_teacher']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Results, ResultsAdmin)
