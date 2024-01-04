from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Departments, Doctors
from .forms import BookingForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)


def doctors(request):
        doctors = [
            {"name": "Dr. Arun", "description": "General Medicine"},
            {"name": "Dr. Thomas", "description": "General Surgery"},
            {"name": "Dr. Anjali", "description": "Neurology"},
            {"name": "Dr. Sreelakshmi", "description": "Pediatrics"},
        ]
        return render(request, 'doctors.html', {'doctorss': doctors})


def contact(request):
    return render(request, 'contact.html')


def department(request):
    departments = [
        {"name": "General Medicine", "description": "Specializing in internal medicine."},
        {"name": "General Surgery", "description": "Expertise in surgical procedures."},
        {"name": "Neurology", "description": "Dealing with disorders of the nervous system."},
        {"name": "Pediatrics", "description": "Focusing on the health of children."},
    ]
    return render(request, 'department.html', {'departments': departments})


def bvmhospital(request):
    return HttpResponse("welcome to bvm hospital")
