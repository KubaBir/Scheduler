from django.contrib import admin

from .models import Availability, Test, User

# Register your models here.
admin.site.register(Test)
admin.site.register(User)
admin.site.register(Availability)
