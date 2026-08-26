from django.shortcuts import render

# Create your views here.

def index(request):
  name = "Alok"
  course = "Django"
  duration  = "4 months"
  return render(request, 'index.html',{"name":name,"course":course , "duration" : duration})