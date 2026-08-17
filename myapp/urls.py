from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('mywebsite/', views.mywebsite, name='mywebsite'),
    path('mystyle/', views.mystyle, name='mystyle'),
    path('voter/<age>', views.voter),  
    path('student', views.student),
    path('teacher', views.teacher),
    
]
