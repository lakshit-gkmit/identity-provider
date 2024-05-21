from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from identity_provider.service_authorization import authorization_access
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from identity_provider.models import Service,Method,MicroService
from identity_provider.serializers import ServiceSerializer
from identity_provider.utils import create_response
from identity_provider.pagination import CustomLimitOffsetPagination


User = get_user_model()



class ServiceAPIView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomLimitOffsetPagination
    
    
    def get(self,request):
        secret_key = request.headers.get('X-API-SECRET-KEY')
        
        if not secret_key:
            return Response(create_response( "Missing API secret key."),status=status.HTTP_403_FORBIDDEN)
        
        
        queryset = Service.objects.filter(micro_service__secret_key=secret_key)
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request, view=self)
        
        
        if page is not None:
            print(page)
            serializer = ServiceSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = ServiceSerializer(queryset, many=True)
        return Response(serializer.data)




    def post(self, request):
        secret_key = request.headers.get('X-API-SECRET-KEY')   
        try:
            ms = MicroService.objects.get(secret_key=secret_key)
        except MicroService.DoesNotExist:
            return Response(create_response( "Missing API secret key."),status=status.HTTP_403_FORBIDDEN)
        
        serializer = ServiceSerializer(data={
            "micro_service":ms.id,
            **request.data
        })

        if(serializer.is_valid()):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(create_response(
            "The request payload is invalid or missing required fields.",
            serializer.errors
        ),status=status.HTTP_400_BAD_REQUEST)

        


    








