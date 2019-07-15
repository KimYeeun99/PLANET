from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser

class CustomAdminUser(UserAdmin,admin.ModelAdmin):
    model = CustomerUser
    list_display = ['email','username','name','nickname','gender','birth_date']

admin.site.register(CustomerUser,CustomAdminUser)