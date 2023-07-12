from django.shortcuts import render, redirect
from.models import Department,Doctors
from . forms import BookingForm
def index(request):
    return render(request,"index.html")
def department(request):
    departments=Department.objects.all()
    return render(request,"department.html",{'departments':departments})
def doctor(request):
    doctors=Doctors.objects.all()
    return render(request,"doctor.html",{'doctors':doctors})
def booking(request):
    form = BookingForm()
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking")
    return render(request,"booking.html",{'form':form})

