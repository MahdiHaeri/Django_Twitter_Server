from django.db import models


# Create your models here.

class Bio(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='bios')
    biography = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id) + " " + self.biography
