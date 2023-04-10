from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #creates a 1 to 1 relationship
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    bio = models.TextField(default='autobiography goes here!')

    def __str__(self):
        return f'{self.user.username} Profile'