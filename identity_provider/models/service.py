from django.db import models
from identity_provider.utils.abstract_models import AbstractModel
from .micro_service import MicroService

class Service(AbstractModel):
    micro_service = models.ForeignKey(MicroService,on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    description = models.TextField()