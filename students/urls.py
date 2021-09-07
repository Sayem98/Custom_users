"""Smart_Education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import StudentView, TeacherView, LoginView, DashboardView, LogoutView, ResultView, ViewStudents
urlpatterns = [
    path('createstudent/', StudentView.as_view(), name='create-student'),
    path('createteacher/', TeacherView.as_view(), name='create-teacher'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('result/', ResultView.as_view(), name='student-result'),
    path('viewstudent/', ViewStudents.as_view(), name='view-students')
]
