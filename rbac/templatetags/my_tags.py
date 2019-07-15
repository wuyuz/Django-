from django import template
from django.conf import settings
from collections import OrderedDict
import re
register = template.Library()


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    menu_dict = request.session.get(settings.MENU_SESSION_KEY)
    url = request.path_info
    od = OrderedDict()
    keys_list = sorted(menu_dict,key=lambda x:menu_dict[x]['weight'],reverse=True)
    
    for key in keys_list:
        od[key] = menu_dict[key]  # 属于浅拷贝
    
    for i in menu_dict.values():
        i['class'] = 'hide'    # 给所有的饿一级菜单添加hide
        for m in i['children']:
            if request.current_menu_id == m['id']:  # 重点在次，这里的m的id是权限表中的唯一标识id，也就是说里面有父id也有子id，那么current_id始终获取的是父id
                m['class'] = 'active'  # 因为浅拷贝，m的修改，od也会变
                i['class'] = ''  # 给当前一级菜单移除
    return {'menu_list': od.values()}

@register.inclusion_tag('rbac/breadcrumb.html')
def breadcrumb(request):
    breadcrumb_list = request.breadcrumb_list
    return {'breadcrumb_list':breadcrumb_list}