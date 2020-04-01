from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser

class CustomAdminUser(admin.ModelAdmin):
    model = CustomerUser
    fields = ['email','password','username','name','nickname','gender','birth_date','message_count']
    search_fields = ['email','username','name','nickname','gender','birth_date','message_count']
    list_display = ['email','username','name','nickname','gender','birth_date','message_count']

admin.site.register(CustomerUser, CustomAdminUser)