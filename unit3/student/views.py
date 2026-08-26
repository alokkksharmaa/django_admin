from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  # name = 'Sumit Kumar'
  # course = 'Django'
  # city = 'Bangalore'
  # courses = ['Python', 'Django', 'Flask', 'JavaScript', 'React']

  database = [
    {"rollno:" : 121, "name": "Sumit Kumar", "city": "Bangalore"},
    {"rollno:" : 122, "name": "Rahul Sharma", "city": "Mumbai"},
    {"rollno:" : 123, "name": "Priya Patel", "city": "Delhi"}
  ]

  return render(request, 'index.html', {'database': database})

  # return render(request, 'index.html', {'username': 'Sumit Kumar','city': city, 'courses': courses })


def about(request):
  return render(request, 'about.html')


def contact(request):
  return render(request, 'contact.html')