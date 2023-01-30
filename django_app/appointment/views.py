from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Appointment,Doctor,Patient,Meeting
from django.contrib import messages


# Create your views here.

def appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        date = request.POST['date']

        appointment = Appointment.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
            date=date,
        )
        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {name} for making an appointment - {phone} - {message}")
        return HttpResponse("request.path successfully")


    return render(request,'appointment.html')
