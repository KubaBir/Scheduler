from django.urls import path

from .views import (AddAvailability, CancelLesson, JoinLesson,
                    ListAvailableLessons, ListMyLessons)

app_name = "lessons"

urlpatterns = [
    path("add/", AddAvailability.as_view(), name="add"),
    path("list/", ListAvailableLessons.as_view(), name="list"),
    path('join/<int:pk>', JoinLesson.as_view(), name='join'),
    path('cancel/<int:pk>', CancelLesson.as_view(), name='cancel'),
    path('booked', ListMyLessons.as_view(), name='booked'),
]
