from django.db import models
from account.models import User
from versatileimagefield.fields import VersatileImageField, PPOIField

class Photo(models.Model):
    user = models.ForeignKey(User, verbose_name=("User Name"), on_delete=models.CASCADE)
    image = VersatileImageField('Images', upload_to = 'images/', ppoi_field= 'image_ppoi')

    image_ppoi = PPOIField()

    def __str__(self):
        return str(self.user)
    
