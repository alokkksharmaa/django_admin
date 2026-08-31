from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  # name = 'Sumit Kumar'
  # course = 'Django'
  # city = 'Bangalore'
  # courses = ['Python', 'Django', 'Flask', 'JavaScript', 'React']

  # database = [
  #   {"rollno:" : 121, "name": "Sumit Kumar", "marks": 85, "Dept": "CSE"},
  #   {"rollno:" : 122, "name": "Rahul Sharma", "marks": 90, "Dept": "ECE"},
  #   {"rollno:" : 123, "name": "Priya Patel", "marks": 95, "Dept": "AI/ML"}
  # ]

  # name = "web development course"
  # desc = "This is a Django project created by Sumit Kumar"
  # return render(request, 'index.html', {'name': name, 'desc': desc})  

  # return render(request, 'index.html', {'database': database})

  # return render(request, 'index.html', {'username': 'Sumit Kumar','city': city, 'courses': courses })

  employees = [
    {"name": "Sumit Kumar", "age": 30, "department": "IT", salary: 60000},
    {"name": "Rahul Sharma", "age": 25, "department": "HR", salary: 50000},
    {"name": "Priya Patel", "age": 28, "department": "Finance", salary: 55000}
  ]

  return render(request, 'index.html', {'employees': employees})


def about(request):
  return render(request, 'about.html')


def contact(request):
  return render(request, 'contact.html')