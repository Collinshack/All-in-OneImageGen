from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Image, CustomUser, QrCode, Waitlist
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('name', 'email', 'api_key')
    search_field = ('name', 'email', 'username')
   

# class CustomUserAdmin(BaseUserAdmin):
#     list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
#     search_field = ('email', 'username',)
#     readonly_field = ('date_joined', 'last_login')
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = () # note to self: required

admin.site.register(Image)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(QrCode)
admin.site.register(Waitlist)
