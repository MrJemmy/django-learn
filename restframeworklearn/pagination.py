from rest_framework.pagination import LimitOffsetPagination, CursorPagination, PageNumberPagination


class ProductListPagePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'records'
    max_page_size = 10
    last_page_strings = 'last'  # ?page=last


class ProductListLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 20


class ProductListCursorPagination(CursorPagination):
    """
    order it based on created field it may not be in our model
    we can not give any offset to start and Limit will be fixed.
    """
    page_size = 5
    ordering = 'id'