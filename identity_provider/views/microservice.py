from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from identity_provider.service_authorization import authorization_access
from identity_provider.models import MicroService
from identity_provider.serializers import MicroServiceSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from identity_provider.utils import create_response
from identity_provider.pagination import CustomLimitOffsetPagination

User = get_user_model()



class MicroServiceAPIView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = MicroService
    serializer = MicroServiceSerializer
    pagination_class = CustomLimitOffsetPagination


    def get_queryset(self):
        return self.queryset.objects.all().order_by("-created_at")

    def get(self,request):
        queryset = self.get_queryset()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request, view=self)
        if page is not None:
            serializer = self.serializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = self.serializer(queryset, many=True)
        return Response(serializer.data)

    # Role yet to define
    def post(self, request):
        request_data = request.data
        serializer = self.serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(create_response(
            "The request payload is invalid or missing required fields.",
            serializer.errors
        ),status=status.HTTP_400_BAD_REQUEST)









