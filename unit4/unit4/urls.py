from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('unit4.myapp.urls')),
]


urlpatterns = [
    path(re_path('student'))
]

# using re_path() create a url that accepts stduent regustration no in the format: CSE2026A001
# the url should reject invalid registration numbers . write urls .py and pattern and view logic 
# create url /result/<student_id/<marks>