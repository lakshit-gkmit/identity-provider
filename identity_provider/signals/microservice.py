import random
import string
from django.db.models.signals import pre_save
from django.dispatch import receiver
from identity_provider.models import MicroService

@receiver(pre_save, sender=MicroService)
def generate_microservice_secret_key(sender, instance, **kwargs):
    if not instance.secret_key:
        secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=59))
        instance.secret_key = secret_key