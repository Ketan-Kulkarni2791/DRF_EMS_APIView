from rest_framework import serializers
from ems_dev.models import Department
from ems_dev.models import Job
from ems_dev.models import Employee
                    

### 2. GET first_name, last_name and salary of the employees.
class specific_columns_employee_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', "last_name", "salary")