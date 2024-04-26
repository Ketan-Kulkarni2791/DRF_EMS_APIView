from rest_framework import serializers
from .models import Department
from .models import Job


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'