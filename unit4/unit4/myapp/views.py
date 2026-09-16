from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  return render(request, "index.html")


def contact(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    return render(request, 'contact.html', {'name':name, 'email':email, 'subject' : subject})
    # print(f"Name: {name}, Email: {email} , Subject: {subject}")
  return render(request, "contact.html")


def login(request):
  if request.method == "POST":
    if request.POST.get("name")=="admin" and request.POST.get("email")=="aloksharma1097@gmail.com" and request.POST.get("password")=="12334":
      return HttpResponse("You are logged in")
    else:
      return HttpResponse("enter your name and password correct")
  return render(request, "login.html")



def index(request):
  return render(request, "index.html")