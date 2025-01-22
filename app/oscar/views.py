from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.contrib import messages
# Create your views here.
# def home(request):
    # return render(request,"index.html")

def contact(request):
    if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       content = request.POST.get('content')
       number = request.POST.get('number')
       print(name,email,content,number)

       if len(name)>1 and len(name)<30:
           pass
       else:
           messages.error(request,"Length of Name Should Be Greater Than 2 and Less Than 30")
           return render(request,"index.html")
       if len(email)>1 and len(email)<30:
           pass
       else:
           messages.error(request,"Invalid Email Try again")
           return render(request,"index.html")
       if len(number)>2 and len(number)<13:
           pass
       else:
           messages.error(request,"Invalid Number")
           return render(request,"index.html")
       usr = Contact(name=name,email=email,number=number,content=content)
       usr.save()
       messages.success(request,"Thankyou For Submitted The Data")

    return render(request,"index.html")