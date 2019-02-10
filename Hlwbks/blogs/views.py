from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# 首页
def index(request):

    return render(request,"blogs/index.html")