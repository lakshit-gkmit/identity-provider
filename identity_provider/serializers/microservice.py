from identity_provider.models import MicroService
from rest_framework import serializers

class MicroServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MicroService
        exclude = ["secret_key"]

    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["secret_key"] = instance.secret_key
        return response