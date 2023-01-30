from django.shortcuts import render
from .models import Products
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView
from django.conf import settings

# Create your views here.
def home(request):
    ducts= Products .objects.all()
    return render(request,'home.html',{'ducts':ducts})

def index(request):
    
    return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        name   = request.POST.get('full-name')
        email  = request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        data={
            'name' :name,
            'email' :email,
            'subject':subject,
            'message':message,

        }

        message = '''
            New message :{}
            From:{}
        '''.format(data['message'],data['email'])

        send_mail(data['subject'],message,'',['toymysmart2015@gmail.com'])
        reply_to=[email]
        print('send success')
        return HttpResponse("email send successfully")


    return render(request,'contact.html',{})



