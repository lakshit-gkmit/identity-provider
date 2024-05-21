from django.db import models
from identity_provider.utils.abstract_models import AbstractModel
from .service import Service
from .method import Method
from .group import Group


class GroupServiceMethod(AbstractModel):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)

