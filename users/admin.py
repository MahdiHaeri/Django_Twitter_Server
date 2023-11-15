from django.contrib import admin
from users.models import CustomUser, Follow, Block


# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'password', 'phone_number',
        'country', 'birthday')


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'follower', 'followed')


class BlockAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'blocker', 'blocked')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Block, BlockAdmin)
