"""gumberoo_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/teachers/', views.TeacherList.as_view()),
    path('api/v1/teachers/<int:pk>/', views.TeacherDetail.as_view()),
    path('api/v1/teachers/<int:pk>/students/', views.TeacherStudent.as_view()),
    path('api/v1/teachers/<int:pk>/lessons/', views.TeacherLesson.as_view()),
    path('api/v1/lessons/<int:pk>/', views.LessonDetail.as_view()),
    path('api/v1/students/<int:pk>/', views.LessonStudentCreation.as_view()),
    path('api/v1/lessons/<int:pk>/average_score/', views.LessonAverage.as_view()),
    path('api/v1/students/<int:pk>/average_score/', views.StudentAverage.as_view()),
    path('api/v1/lessons/<int:pk>/students/<int:pk2>/', views.LessonStudentDetail.as_view()),
    path('api/v1/lessonstudents/<int:pk>/', views.LessonStudentList.as_view()),
    path('api/v1/lessons/<int:pk>/zscores/', views.StudentZScores.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
