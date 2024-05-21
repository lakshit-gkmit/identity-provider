from django.apps import AppConfig


class IdentityProviderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "identity_provider"

    def ready(self):
        import identity_provider.signals  
