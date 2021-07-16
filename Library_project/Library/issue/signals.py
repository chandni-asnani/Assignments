from django.db.models.signals import post_save
from django.dispatch import receiver
from issue.models import UserIssuing

@receiver(post_save, sender=UserIssuing)
def signup(sender,instance,created,**kwargs):
    print("Book issued Successfull!")

