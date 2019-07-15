from django.urls import reverse
from django.shortcuts import HttpResponse,render,redirect
from rbac import models
from rbac.service.init_permission import init_permission


def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.User.objects.filter(username=username,pwd=password).first()
        if not obj:
            return render(request,'login.html',{'error':'用户密码错误'})
        init_permission(request,obj)
        return redirect(reverse('index'))
    return render(request,'login.html')
    

def index(request):
    return render(request,'index.html')