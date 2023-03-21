from rest_framework.pagination import PageNumberPagination

from .constants import AMOUNT_OF_PUBLICATIONS


class CustomPageNumberPagination(PageNumberPagination):
    page_size = AMOUNT_OF_PUBLICATIONS
    page_size_query_param = 'limit'

