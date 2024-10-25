from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #default gozashtim time alan bede behesh age nadim khodemon
    date_posted = models.DateField(default=timezone.now)
    #vaqti user delete mishe post bahash delete beshe
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        #vase ine ke ba shell object migiri in chiz ziro neshon bede
        return self.title
    

    #darim ye reverese misazim vase post jadid ke sakhte mishe baadesh berim be detailesh
    def get_absolute_url(self):
        return reverse("post-detail", kwargs= {"pk": self.pk})