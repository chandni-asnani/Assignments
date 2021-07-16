from django.db.models.signals import post_save
from django.dispatch import receiver
from registration.models import User


@receiver(post_save, sender=User)
def signup(sender,instance,created,**kwargs):
    if created:
        print("SignUp Successfull!")

