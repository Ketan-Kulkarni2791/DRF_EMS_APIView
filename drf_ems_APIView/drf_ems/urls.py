from django.contrib import admin
from django.urls import path
from ems_dev import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departmentapi/', views.DepartementAPIView.as_view()),
    path('departmentapi/<int:pk>/', views.DepartementAPIView.as_view()),
    path('jobapi/', views.JobAPIView.as_view()),
    path('jobapi/<int:pk>/', views.JobAPIView.as_view()),
    path('employeeapi/', views.EmployeeAPIView.as_view()),
    path('employeeapi/<int:pk>/', views.EmployeeAPIView.as_view()),
]
