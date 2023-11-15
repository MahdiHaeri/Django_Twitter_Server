from django.contrib import admin

from users.models import User, Follow, Block


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'firstName', 'lastName', 'email', 'password', 'phoneNumber',
        'country', 'birthday', 'created_at', 'updated_at')


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'follower', 'followed', 'created_at', 'updated_at')


class BlockAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'blocker', 'blocked', 'created_at', 'updated_at')


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Block, BlockAdmin)
