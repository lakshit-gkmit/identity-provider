from django.contrib import admin
from .models import Service, Method, UserServiceMethod, Group, UserGroup,GroupServiceMethod,MicroService


admin.site.register(Service)
admin.site.register(Method)
admin.site.register(MicroService)
admin.site.register(UserServiceMethod)
admin.site.register(GroupServiceMethod)
admin.site.register(Group)
admin.site.register(UserGroup)
