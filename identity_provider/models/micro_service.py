from django.db import models
from identity_provider.utils.abstract_models import AbstractModel


class MicroService(AbstractModel):
    secret_key = models.CharField(max_length=60)
    micro_service_name = models.CharField(max_length=100)
    description = models.TextField()



    def __str__(self) -> str:
        return self.micro_service_name