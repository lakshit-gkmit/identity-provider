from django.db import models
from identity_provider.utils.abstract_models import AbstractModel


class Method(AbstractModel):
    method_name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self) -> str:
        return self.method_name