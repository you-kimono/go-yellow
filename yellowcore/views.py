from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    page = '<html><title>go-yellow</title></html>'
    return HttpResponse(page)
