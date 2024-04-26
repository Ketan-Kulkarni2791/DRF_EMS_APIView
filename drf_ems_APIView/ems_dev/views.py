from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department
from .models import Job
from .serializers import DepartmentSerializer
from .serializers import JobSerializer
from rest_framework import status


class DepartementAPIView(APIView):
    """This the view to perform CRUD operations regarding department data."""
    def get(self, request, pk=None, format=None):
        
        id = pk
        if id is not None:
            dept = Department.objects.get(id=id)
            serializer = DepartmentSerializer(dept)
            return Response(serializer.data)
        dept = Department.objects.all()
        serializer = DepartmentSerializer(dept, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Department detail added successfully!'}, 
                             status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id = pk
        dept = Department.objects.get(id=id)
        serializer = DepartmentSerializer(dept, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Department detail updated successfully!'}, 
                             status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)
        
    def patch(self, request, pk, format=None):
        id = pk
        dept = Department.objects.get(id=id)
        serializer = DepartmentSerializer(dept, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Department detail added successfully!'}, 
                             status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        department_id = pk
        dept = Department.objects.get(department_id=department_id)
        dept.delete()
        return Response({'msg': 'Department deleted successfully!'})
    

class JobAPIView(APIView):
    """This the view to perform CRUD operations regarding job data."""
    def get(self, request, pk=None, format=None):
        
        id = pk
        if id is not None:
            job = Job.objects.get(id=id)
            serializer = JobSerializer(job)
            return Response(serializer.data)
        job = Job.objects.all()
        serializer = JobSerializer(job, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Job detail added successfully!'}, 
                             status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id = pk
        job = Job.objects.get(id=id)
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Job detail updated successfully!'}, 
                             status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)
        
    def patch(self, request, pk, format=None):
        id = pk
        job = Job.objects.get(id=id)
        serializer = JobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Job detail added successfully!'}, 
                             status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        job_id = pk
        job = Job.objects.get(job_id=job_id)
        job.delete()
        return Response({'msg': 'Job deleted successfully!'})
    
    