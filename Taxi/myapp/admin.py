# In admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Client, TaxiDriver

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Client)
admin.site.register(TaxiDriver)
