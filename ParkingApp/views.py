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
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(data = request.data)
        return Response(serializer.data)
    
    def post(self, request):
        pass