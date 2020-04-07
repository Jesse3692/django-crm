from django.shortcuts import render, HttpResponse, redirect, reverse
from crm import models

# Create your views here.

# 主页
def index(request):
    return HttpResponse('这是主页')

# 注册
def register(request):
    return render(request, 'register.html')

# 登录
def login(request):
    # print(request.POST)
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        obj = models.UserProfile.objects.filter(username=user, password=pwd, is_active=True).first()
        print('>>>>>>>>>>>>>>>>',obj)
        if obj:
            # 如果登录成功则跳转到主页
            return redirect(reverse('index'))
        else:
            # 登录失败
            return render(request, 'login.html', {'login_error':'用户名或密码错误'})
        return render(request, 'login.html', {'login_error':'用户名或密码错误'})
    else:
        return render(request, 'login.html')
