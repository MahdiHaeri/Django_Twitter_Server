from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName + " " + self.lastName


class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    follower_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='followers')
    followed_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='follows')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.follower_id) + " follows " + str(self.followee_id)


class Block(models.Model):
    id = models.AutoField(primary_key=True)
    blocker_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='blockers')
    blocked_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='blocks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.blocker_id) + " blocks " + str(self.blocked_id)