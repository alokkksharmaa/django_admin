from django.urls import re_path

from . import views

urlpatterns = [
    re_path(
        # r"^result/(?P<student_id>CSE\d{4}[A-Z]\d{3})/(?P<marks>\d{1,3})/$",
        views.result,
        name="student-result",
    ),
]
