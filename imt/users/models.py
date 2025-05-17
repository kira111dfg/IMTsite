from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
    name=models.CharField(max_length=100)
    avatar=models.ImageField(default='img/avatar.jpg',upload_to='img/')
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

