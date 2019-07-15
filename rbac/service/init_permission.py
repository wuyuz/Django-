
from django.conf import settings
def init_permission(request,obj):
    permissions = obj.role.filter(permission__url__isnull=False).values(
        'permission__url',
        'permission__title',
        'permission__menu__icon',
        'permission__menu__title',
        'permission__menu__id'
    ).distinct()  # 获取所有权限表中的信息
    print(permissions)
    # 保存权限信息的列表
    permission_list = []
    # 菜单信息列表
    menu_dic = {}
    
    for i in permissions:
        permission_list.append({'url': i['permission__url']})
        
        menu_id = i.get('permission__menu__id')
        if not menu_id:continue
        
        if menu_id not in menu_dic:
            menu_dic[menu_id]={
                'title': i.get('permission__menu__title'),
                'icon':  i.get('permission__menu__icon'),
                'children':[
                    {'title': i.get('permission__title'),'url': i.get('permission__url')}
                ]
            }
        else:
            menu_dic[menu_id]['children'].append({'title': i.get('permission__title'),'url': i.get('permission__url')})

    request.session[settings.PERMISSION_SESSION_KEY] = permission_list  # 全部存入session中
    request.session[settings.MENU_SESSION_KEY] = menu_dic  # 引用全局setting变量
    request.session['is_login'] = True