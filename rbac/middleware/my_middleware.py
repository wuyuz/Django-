from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import render, redirect,HttpResponse
import re
from django.conf import settings

class Auth(MiddlewareMixin):
    def process_request(self,request):
        # 获取当前path
        path = request.path_info
        # 设置白名单
        for url in settings.WHITE_LIST:
            if re.match(url,path):
                return
            
        # 登陆状态验证
        is_login = request.session.get('is_login')
        if not is_login:
            return redirect(reverse('login'))
        
        for url in settings.NO_PERMISSION_LIST:
            if re.match(url,path):
                return
        permissions = request.session.get('permissions')
        for permission in permissions:
            if re.match(permission['url'],path):
                return
        return HttpResponse('没有权限，请联系管理员')
        