from django.db import models
from django.db.models import CheckConstraint


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.department_name
    
    
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=100, blank=False, null=False)
    min_salary = models.PositiveIntegerField()
    max_salary = models.PositiveIntegerField()
    
    class Meta:
        constraints = [
                CheckConstraint(check=models.Q(min_salary__gt=0), name='check_min_salary'),
                CheckConstraint(check=models.Q(max_salary__gt=0), name='check_max_salary')
        ]
        
    
    def __str__(self) -> str:
        return self.job_title


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100)
    salary = models.IntegerField(blank=False, null=False)
    department_id = models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, related_name='job', on_delete=models.CASCADE)
    