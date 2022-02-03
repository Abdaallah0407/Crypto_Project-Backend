from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class PaginationProducts(PageNumberPagination):
    page_size = 12
    max_page_size = 1000