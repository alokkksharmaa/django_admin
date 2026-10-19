from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        return render(request, "contact.html", {"name": name, "email": email, "subject": subject})
    # print(f"Name: {name}, Email: {email} , Subject: {subject}")
    return render(request, "contact.html")


def login(request):
    if request.method == "POST":
        if request.POST.get("name") == "admin" and request.POST.get("email") == "aloksharma1097@gmail.com" and request.POST.get("password") == "12334":
            return HttpResponse("You are logged in")
        else:
            return HttpResponse("enter your name and password correct")
    return render(request, "login.html")


# import form
from .forms import userForm


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        course = request.POST.get("course")
        message = "Form Submitted"
        return render(
            request,
            "index.html",
            {
                "name": name,
                "phone": phone,
                "city": city,
                "course": course,
                "message": message,
            },
        )
    else:
        form = userForm()
    return render(request, "index.html", {"form": form})



def form(request):
    data = {"method": request.method}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name)
        print(email)
        print(phone)
        print(message)
        return redirect("result")
    return render(request, "form.html", data)


def result(request):
    return render(request, "result.html")