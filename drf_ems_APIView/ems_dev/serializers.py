from rest_framework import serializers
from .models import Department
from .models import Job
from .models import Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    # Add the related_name from the respective models
    department = DepartmentSerializer(read_only=True, many=True)
    job = JobSerializer(read_only=True, many=True)
    class Meta:
        model = Employee
        fields = '__all__'