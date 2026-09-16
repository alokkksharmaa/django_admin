from django.urls import path
from . import views

urlpatterns = [
    # path("index/", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
]


urlpatterns = [
    path("index/",views.index, name="index")
]

urlpatterns= [
    path("userForm/", views.index, name="userform")
]