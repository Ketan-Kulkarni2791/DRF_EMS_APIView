from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q
from django.core.serializers import serialize
from django.http import JsonResponse
import json

from ems_dev.models import Department
from ems_dev.models import Job
from ems_dev.models import Employee
from ems_dev.serializers import DepartmentSerializer
from ems_dev.serializers import JobSerializer
from ems_dev.serializers import EmployeeSerializer
from .serializers import (specific_columns_employee_list_serializer,
                          distinct_clause_employee_salary_serializer,
                        )



### 1. GET all the employees details.
@api_view(['GET'])
def employee_list(request):
    emp = Employee.objects.all()
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)


### 2. GET first_name, last_name and salary of the employees.
@api_view(['GET'])
def specific_columns_employee_list(request):
    emp = Employee.objects.all()
    serializer = specific_columns_employee_list_serializer(emp, many=True).data
    return Response(serializer)


### 3. GET all the employees whose salary is greater than or equal to 200000.
@api_view(['GET'])
def gt_lookup_employee_salary(request):
    emp = Employee.objects.filter(salary__gt=200000)
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)


### 4. GET the employees where last_name = ‘Kulkarni’ and salary = 300000.
@api_view(['GET'])
def or_operator_employee_list(request):
    emp = Employee.objects.filter(
        Q(last_name = 'Kulkarni') | Q(salary=300000)
    )
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)


### 5. GET the employees whose salary is either 3 lacs or 1.5 lacs.
@api_view(['GET'])
def or_operator_employee_salary(request):
    emp = Employee.objects.filter(
        Q(salary=150000) | Q(salary=300000)
    )
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)


### 6. GET the employee first names that start with K.
@api_view(['GET'])
def startswith_operator_employee_names(request):
    emp = Employee.objects.filter(first_name__startswith='K')
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)


### 7. GET the employee first names that have i in any position.
@api_view(['GET'])
def contains_operator_employee_names(request):
    emp = Employee.objects.filter(first_name__contains='i')
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)

### 8. GET the employee first name that ends with 'a'.
@api_view(['GET'])
def endswith_operator_employee_names(request):
    emp = Employee.objects.filter(first_name__endswith='a')
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)

### 9. GET the employee details of 'Rachit', 'Ketan', 'Manoj', 'Shubham'.
@api_view(['GET'])
def in_operator_employee_names(request):
    emp = Employee.objects.filter(Q(first_name__in=('Rachit', 'Ketan', 'Manoj', 'Shubham')))
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)

### 10. GET the employee details other than 'Rachit', 'Ketan', 'Manoj', 'Shubham'.
@api_view(['GET'])
def not_in_operator_employee_names(request):
    emp = Employee.objects.filter(~Q(first_name__in=('Rachit', 'Ketan', 'Manoj', 'Shubham')))
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)

### 11. GET the employee details where salary is salary BETWEEN 200000 AND 300000.
@api_view(['GET'])
def between_operator_employee_salary(request):
    emp = Employee.objects.filter(salary__range=(200000, 300000))
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)

### 12. GET distinct salary of the employees.
@api_view(['GET'])
def distinct_clause_employee_salary(request):
    emp = Employee.objects.all().distinct("salary")
    serializer = distinct_clause_employee_salary_serializer(emp, many=True)
    return Response(serializer.data)

### 13. GET employee details in descending order of salary.
@api_view(['GET'])
def orderby_clause_employee_salary(request):
    emp = Employee.objects.all().order_by('-salary')
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)

### 14. GET the employees details with their respective departments.
@api_view(['GET'])
def emp_dept_detail_employee_list(request):
    emp = Employee.objects.select_related('department_id')\
        .values('employee_id', 'first_name', 'last_name', 'salary', 'department_id__department_name')
    employee_dept_data = [e for e in emp]
    return JsonResponse(employee_dept_data, safe=False)