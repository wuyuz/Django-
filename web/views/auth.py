from django.shortcuts import render, reverse, redirect

from rbac import models
from rbac.service.init_permission import init_permission


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.User.objects.filter(username=username, password=password).first()
        if not obj:
            return render(request, 'login.html', {'error': '用户名或密码错误'})
        # 登录成功
        # 权限和菜单信息的初始化
        init_permission(request, obj)

        return redirect(reverse('index'))

    return render(request, 'login.html')
