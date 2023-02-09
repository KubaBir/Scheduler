from django.urls import path

from .views import AddAvailability

app_name = "lessons"

urlpatterns = [
    path("add/", AddAvailability.as_view(), name="add"),
]
