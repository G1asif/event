from django.shortcuts import render
from .models import table
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'index.html')
def book(request):
    return render(request,'book.html')
def home1(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    mobile=request.POST.get("mobile")
    gender=request.POST.get("gender")
    eventname=request.POST.get("eventname")
    order=table(name=name,email=email,mobile=mobile,gender=gender,eventname=eventname)
    order.save()
    # subject = 'Event Conformation'
    # message = f'Your Event Is Booking Succesfully'
    # from_email ='bgmigameforyou@gmail.com'
    # send_mail(subject,message,from_email,[email])
    return render(request,'index.html')
def chat(request):
    return render(request,'chat.html')
