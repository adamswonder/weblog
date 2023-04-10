from tkinter import Image
import PIL.Image # Lets you open image files
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #creates a 1 to 1 relationship
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    bio = models.TextField(default='autobiography goes here!')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # overrides the parent save method
    def save(self):
        super().save()

        img = PIL.Image.open(self.image.path) # type: ignore

        # checks image dimensions 
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# TODO: Delete old images when user uploads a new profile picture