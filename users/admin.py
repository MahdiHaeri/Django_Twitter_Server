from django.contrib import admin

from users.models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'firstName', 'lastName', 'email', 'password', 'phoneNumber',
        'country', 'birthday', 'created_at', 'updated_at')


admin.site.register(User, UserAdmin)
