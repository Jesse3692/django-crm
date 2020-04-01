from django.shortcuts import render, HttpResponse

# Create your views here.

# 主页
def index(request):
    return HttpResponse('这是主页')
