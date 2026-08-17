from django.contrib import admin
from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('myapp/', include('myapp.urls')),
    # path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    # path("student1/", views.student1, name='student1'),
    path("check/", views.check, name='check'),
    path("course/<str:course_name>/", views.course, name='course'),
    path('emp/<int:emp_id>/<str:emp_name>/', views.emp, name='employee'),
    path('website1/<int:id>/', views.website1),
    path('website2/<slug:id>/', views.website2),
    # path('about/', views.about),
    re_path(r"^about/$",views.about),
    # re_path(r"^blog/(?P<id>[0-9]+)/$",views.blog),
    # re_path(r"blog/(?P<id>[a-z]+)/$", views.blog),
    re_path(r"blog/(?P<id>[a-z0-9A-Z]/$)", views.blog),
    path("blog/", views.blog),
    path("profile/", views.profile),
    path("student/", views.studentinfo),
    path("sum/", views.sum),
]

# a powerful string-matching tool used to build flexible URL patterns, 
# enforce strict form data validation, and execute advanced database queries