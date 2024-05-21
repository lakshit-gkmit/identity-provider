from django.db import models
from identity_provider.utils.abstract_models import AbstractModel
from .service import Service
from .method import Method
from django.contrib.auth import get_user_model

User = get_user_model()

class UserServiceMethod(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)