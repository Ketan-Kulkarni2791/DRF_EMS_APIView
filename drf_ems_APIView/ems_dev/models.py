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

