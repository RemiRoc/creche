from django.contrib import admin

from account_mgt.models import  User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email','first_name','last_name','phone_number','company','address','date_joined','is_active')
    fields = ('email','first_name','last_name','is_staff','is_active','password')

admin.site.register(User, UserAdmin)
