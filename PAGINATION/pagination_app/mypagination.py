from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

# class MyPageNumberPAgination(PageNumberPagination):
#     page_size = 5
#     page_query_param = 'pag'
#     #this is for client to display how many records
#     page_size_query_param = 'records'
#     max_page_size = 6
#     last_page_strings = 'end'

# class MyLimitOffsetPagination(LimitOffsetPagination):
#      default_limit = 4
#      limit_query_param = 'mylimit'
#      offset_query_param = 'myoffset'
#      max_limit = 3

class MyCursorPagination(CursorPagination):
     page_size = 5
     ordering = 'name'
     cursor_query_param = 'cu'
