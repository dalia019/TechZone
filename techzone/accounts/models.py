from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='admin_profiles/', null=True, blank=True)
    position = models.CharField(max_length=100, default='Admin')

    def __str__(self):
        return self.user.username
