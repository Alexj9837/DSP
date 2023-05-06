from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Custom_user

# Register your models here.
admin.site.register(Custom_user, UserAdmin)