from rest_framework import serializers
from .models import Company_name, Employee, Vehicle, ParkingSlot, ParkingTicket


class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_name
        fields = ['id', 'name', 'address']
        read_only_fields = ['id']
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "_all_"