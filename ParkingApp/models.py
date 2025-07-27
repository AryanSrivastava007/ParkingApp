from django.db import models

class Company_name(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company_name, on_delete=models.CASCADE)
    
class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    license_plate = models.CharField(max_length=15)
    vehicle_type = models.CharField(max_length=50)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
class ParkingSlot(models.Model):
    id = models.IntegerField(primary_key=True)
    slot_number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default = False)
    company_id = models.ForeignKey(Company_name, on_delete=models.CASCADE)

class ParkingTicket(models.Model):
    id = models.IntegerField(primary_key=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    slot_id = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    car_photo = models.ImageField(upload_to='car_photos/', null=True, blank=True)
