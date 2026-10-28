from django.contrib import admin
from django.urls import path
from studentApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("std/", views.reg, name="student-registration"),
    path("success/", views.success, name="success"),
    path("depart/", views.depart, name="departments"),
]
