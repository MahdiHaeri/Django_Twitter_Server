from django.contrib import admin
from users.models import CustomUser, Follow, Block


# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'password', 'phone_number',
        'country', 'birthday', 'created_at', 'updated_at')


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'follower', 'followed', 'created_at', 'updated_at')


class BlockAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'blocker', 'blocked', 'created_at', 'updated_at')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Block, BlockAdmin)
