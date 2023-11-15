from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class CustomUser(AbstractUser, PermissionsMixin):
    phone_number = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    birthday = models.DateField(null=True)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    follower = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='followers')
    followed = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='follows')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.follower_id) + " follows " + str(self.followed_id)


class Block(models.Model):
    id = models.AutoField(primary_key=True)
    blocker = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='blockers')
    blocked = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='blocks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.blocker_id) + " blocks " + str(self.blocked_id)
