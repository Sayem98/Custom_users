from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import status

from django.views import View
from .forms import StudentSingUpForm, TeacherSingUpForm, AddResultForm
from rest_framework.response import Response
from .models import Student, Teacher, Results
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

User = get_user_model()


class StudentView(View):
    def get(self, request):
        form = StudentSingUpForm()
        return render(request, 'students/html/student_signup.html', {
            'form': form,
            'has_permission_to_add_student': True
        })

    def post(self, request):
        form = StudentSingUpForm(request.POST)
        has_permission_to_add_student = True
        if request.user.is_authenticated:
            if request.user.has_perm('students.add_student'):

                if form.is_valid():
                    form.save()
                    user = User.objects.filter(username=form.cleaned_data.get('username'))[0]
                    print(user)
                    user.is_student = True
                    user.save()
                    my_group = Group.objects.get(name='student')
                    my_group.user_set.add(user)
                    student = Student.objects.create(roll=form.cleaned_data.get('roll'), user=user)
                    student.save()
                    return redirect('user-login')

                return render(request, 'students/html/student_signup.html', {
                    'form': form,
                    'has_permission_to_add_student': has_permission_to_add_student
                })
            else:
                return render(request, 'students/html/student_signup.html', {
                    'form': form,
                    'has_permission_to_add_student': False
                })

        else:
            return redirect('user-login')


class TeacherView(View):
    def get(self, request):
        form = TeacherSingUpForm()
        return render(request, 'students/html/teacher_signup.html', {
            'form': form
        })

    def post(self, request):
        form = TeacherSingUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.filter(username=form.cleaned_data.get('username'))[0]
            # print(user)
            user.is_teacher = True
            user.save()
            my_group = Group.objects.get(name='teacher')
            my_group.user_set.add(user)

            teacher = Teacher.objects.create(teacher_id=form.cleaned_data.get('teacher_id'), user=user)
            teacher.save()
            return redirect('user-login')
        return render(request, 'students/html/teacher_signup.html', {
            'form': form
        })


class LoginView(View):
    def get(self, request):
        invalid_user = False
        form = AuthenticationForm()
        return render(request, 'students/html/user_login.html', {
            'form': form,
            'invalid_user': invalid_user
        })

    def post(self, request):
        invalid_user = False
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                invalid_user = True
        return render(request, 'students/html/user_login.html', {
            'form': form,
            'invalid_user': invalid_user
        })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user-login')


class DashboardView(View):
    def get(self, request):
        if request.user.is_student:
            return render(request, 'students/html/student_dashbord.html')
        if request.user.is_teacher:
            return render(request, 'students/html/teacher_dashbord.html')
        else:
            return redirect('user-login')


class ResultView(View):
    def get(self, request):
        result_add_form = AddResultForm()
        return render(request, 'students/html/results.html', {
            'result_add_form': result_add_form,
            'result_add_perm': True

        })

    def post(self, request):
        result_add_form = AddResultForm(request.POST)
        if request.user.is_authenticated:
            if result_add_form.is_valid():
                if request.user.has_perm('students.add_Results'):
                    print(result_add_form.cleaned_data)

                    student_user_name = result_add_form.cleaned_data.get('student')

                    user_by_student_user_name = User.objects.filter(username=student_user_name)[0]

                    student = user_by_student_user_name.student
                    print(student.roll)

                    result = Results(student=student,
                                     cgpa=result_add_form.cleaned_data.get('cgpa'))
                    result.save()
                    return redirect('student-result')
                else:
                    return render(request, 'students/html/results.html', {
                        'result_add_form': result_add_form,
                        'result_add_perm': False
                    })
            return render(request, 'students/html/results.html', {
                'result_add_form': result_add_form,
                'result_add_perm': True
            })
        return redirect('user-login')


class ViewStudents(View):
    def get(self, request):
        if request.user.is_authenticated:

            if request.user.has_perm('students.view_student'):
                # print(request.user.groups.all())

                students = Student.objects.filter()
                print(students)
                return render(request, 'students/html/viewstudents.html', {
                    'students': students,
                    'has_permission_view_student': True

                })

            return render(request, 'students/html/viewstudents.html', {
                'students': [],
                'has_permission_view_student': False

            })
        return redirect('user-login')