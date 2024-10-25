from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pic")

    def __str__(self) -> str:
        return f"{self.user.username} profile!"
    
    #vaqti ax upload shod save mikonim baad resizesh mikonm
    def save(self, *args, **kwargs):
        #save parent injori active mikonim
        super().save(*args, **kwargs)
        # image current instance injori open mikonim hamon ke save shode
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            #inke ba self hasto override mikone
            img.save(self.image.path)