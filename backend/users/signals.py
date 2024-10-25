from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import profile
from django.dispatch import receiver
#bayd to app.py import beshe ina


#create_profile harvaqt User create beshe inam bahash run mishe baraye on user profile misaze
@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)


#harvat user object save beshe in profile ham bahash save mishe
@receiver(post_save, sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()