from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # расширенная модель User

admin.site.register(CustomUser, UserAdmin)
