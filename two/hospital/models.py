from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    def __str__(self):
        return self.name
    
class Doctors(models.Model):
    name=models.CharField(max_length=50)
    spc=models.CharField(max_length=10)
    dep=models.ForeignKey(Department, on_delete=models.CASCADE)
    image=models.CharField(max_length=500)
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    p_name=models.CharField(max_length=50)
    p_email=models.CharField(max_length=20)
    p_phone=models.CharField(max_length=30)
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField() 
    def __str__(self):
        return self.p_name           