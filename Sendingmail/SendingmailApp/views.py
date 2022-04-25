from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hello Priyanka',
    'Hello there,this is an automated message',
    'priyankazanjad95@gmail.com',
    ['priyankazanjad5@gmail.com'],
    fail_silently=False
              )

    return render(request,'SendingmailApp/index.html')
