from django.db import models
from identity_provider.utils.abstract_models import AbstractModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(AbstractModel):
    group_name = models.CharField(max_length=100)
    description = models.TextField()


class UserGroup(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)