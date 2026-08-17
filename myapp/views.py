from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. Welcome to homepage of Myapp!")
# def home(request):
#     return HttpResponse("hello from home")

def about(request):
    return HttpResponse("Hello from myapp/about!")

def contact(request):
    return HttpResponse("Hello from myapp/contact!")

def mywebsite(req):
    return HttpResponse('<h1>Welcome to my website!</h1>')

def mystyle(req):
    return HttpResponse('<h1 style="color:lime;">Welcome to my website with style!</h1>')



def mylist_view(req):
  mylist = ['Home', 'About', 'Contact', 'My Website', 'My Style']
  for item in mylist:
    print(item)
    return HttpResponse(item)


def mylist(req):
  return HttpResponse("""
  <ul>
  <li> Python </li>
  <li> Java </li>
  <li> C++ </li>
  </ul>
  """)


def addscript(req):
    return HttpResponse(""<script>alert('hello from js')<script>"")

def student1(request, value):
    return HttpResponse("Welcome to the Home")

def voter(request, age):
    age = int(age)
    if age >= 18:
        return HttpResponse("You are eligible for vote!")
    else:
        return HttpResponse("You are  not eligible for vote!")

def student(req):
    return HttpResponse("<h1>Welcome to the student page!</h1>")

def teacher(req):
    return HttpResponse("<h1> Welcome to the teacher page </h1>")

