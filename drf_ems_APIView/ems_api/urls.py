from django.urls import path
from . import views


urlpatterns = [
    path('emp_list/', views.employee_list),
    path('specific_col_emp_list/', views.specific_columns_employee_list),
    path('gt_lookup_employee_salary/', views.gt_lookup_employee_salary),
    path('or_operator_employee_list/', views.or_operator_employee_list),
    path('or_operator_employee_salary/', views.or_operator_employee_salary),
    path('startswith_operator_employee_names/', views.startswith_operator_employee_names),
    path('contains_operator_employee_names/', views.contains_operator_employee_names),
    path('endswith_operator_employee_names/', views.endswith_operator_employee_names),
    path('in_operator_employee_names/', views.in_operator_employee_names),
    path('not_in_operator_employee_names/', views.not_in_operator_employee_names),
]

