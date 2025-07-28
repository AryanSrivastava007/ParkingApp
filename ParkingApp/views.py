from django.shortcuts import render
from django.http import HttpResponse
from .models import Company_name, Employee, Vehicle, ParkingSlot, ParkingTicket
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import CompanyNameSerializer, EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CompanyNameAPIView(APIView):
    def get(self, request):
        # companies = Company_name.objects.all()
        # serializer = CompanyNameSerializer(companies, many=True)
        # return Response(serializer.data)
        company_id = request.query_params.get('id')
        if company_id:
            try:
                company = Company_name.objects.get(id = company_id)
                serializer = CompanyNameSerializer(company)
                return Response(serializer.data)
            except Company_name.DoesNotExist:
                return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            companies = Company_name.objects.all()
            serializer = CompanyNameSerializer(companies, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = CompanyNameSerializer(data=request.data)
        if serializer.is_valid():
            company = serializer.save()
            return Response({"name": company.name, "address": company.address}, status=201)
        return Response(serializer.errors, status=400)
    
class EmployeeAPIView(APIView):
    def get(self, request):
        employee_id = request.query_params.get('id')
        if employee_id:
            try:
                employee = Employee.objects.get(id = employee_id)
                serializer = EmployeeSerializer(employee)
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            employee = serializer.save()
            return Response({"name": employee.name, "company_id": employee.company_id.id})
        return Response(serializer.errors, status=400)
