from functools import wraps
from django.http import HttpResponseForbidden



def user_has_access(user, service_name, method_name):
    return user.userservicemethod_set.filter(service__service_name=service_name, method__method_name=method_name).exists()
    

def group_has_access(groups, service_name, method_name):
    # Your logic to check if any of the user's groups have access to the service and method
    # Example:
    for group in groups:
        if group.groupservicemethod_set.filter(service__service_name=service_name, method__method_name=method_name).exists():
            return True
    return False




def authorization_access(service_name, method_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request ,*args, **kwargs):
            # Check if user has access to the service and method
            if user_has_access(request.user, service_name, method_name) or \
               group_has_access(request.user.groups.prefetch_related("groupservicemethod_set").all(), service_name, method_name):
                # User has access, call the view function
                return view_func(request, *args, **kwargs)
            else:
                # User does not have access, return forbidden response
                return HttpResponseForbidden("You don't have permission to access this resource.")
        return wrapper
    return decorator

