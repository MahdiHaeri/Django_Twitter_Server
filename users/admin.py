from django.contrib import admin

from users.models import User, Follow, Block


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'firstName', 'lastName', 'email', 'password', 'phoneNumber',
        'country', 'birthday', 'created_at', 'updated_at')


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'follower_id', 'followed_id', 'created_at', 'updated_at')


class BlockAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'blocker_id', 'blocked_id', 'created_at', 'updated_at')


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Block, BlockAdmin)
