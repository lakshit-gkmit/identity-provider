from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10  # Default number of items per page
    max_limit = 100     # Maximum number of items per page
    limit_query_param = 'limit'    # URL query parameter for limit
    offset_query_param = 'offset'  # URL query parameter for offset
    max_limit_query_param = 'max_limit'  # URL query parameter for max_limit

    def get_limit(self, request):
        limit = super().get_limit(request)
        if limit is None:
            return self.max_limit
        return min(int(limit), self.max_limit)