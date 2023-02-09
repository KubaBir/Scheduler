from django.urls import path

from .views import testView

app_name = 'core'

urlpatterns = [
    path('test/', testView, name='index')
]
