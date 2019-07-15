from django.conf import settings


def init_permission(request, obj):
    # 获取权限
    permissions = obj.roles.filter(permissions__url__isnull=False).values(
        'permissions__url',
        'permissions__title',
        'permissions__menu__title',
        'permissions__menu__icon',
        'permissions__menu_id',
        'permissions__menu__weight',
        'permissions__id',  # 拿出权限id
        'permissions__parent_id',  # 拿出父权限id
    ).distinct()
    
    # 权限信息的列表
    permission_dict = {}
    # 菜单信息的列表
    menu_dict = {}
    
    for i in permissions:  # {  'permissions__url', ...}
        #  存入所有的信息，包括了每个权限的id和父id
        permission_dict[i['permissions__id']]={'url': i['permissions__url'], 'id': i['permissions__id'], 'pid': i['permissions__parent_id'],
             'title': i.get('permissions__title')}
        
        menu_id = i.get('permissions__menu_id')
        if not menu_id:
            continue
        
        if menu_id not in menu_dict:
            # menu_dict 用于生成菜单每一个标签
            menu_dict[menu_id] = {
                'title': i.get('permissions__menu__title'),
                'icon': i.get('permissions__menu__icon'),
                'weight': i.get('permissions__menu__weight'),
                'children': [
                    # 存入父id，以便于作比较
                    {'title': i.get('permissions__title'), 'url': i.get('permissions__url'),
                     'id': i.get('permissions__id')}
                ]
            }
        else:
            menu_dict[menu_id]['children'].append(
                {'title': i.get('permissions__title'), 'url': i.get('permissions__url')})
    
    # 保存到session中
    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict  # json序列化
    request.session[settings.MENU_SESSION_KEY] = menu_dict  # json序列化
    request.session['is_login'] = True
