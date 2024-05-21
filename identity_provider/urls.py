from django.urls import path
from .views import MicroServiceAPIView,ServiceAPIView


urlpatterns = [
    path("micro-service/",MicroServiceAPIView.as_view(),name="micro_service"),
    path("service/",ServiceAPIView.as_view(),name="service")
]
