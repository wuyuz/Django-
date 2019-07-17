data = [{
    'permissions__url': '/customer/list/',
    'permissions__title': '客户列表',
    'permissions__menu__title': '客户管理',
    'permissions__menu__icon': 'fa-user-o',
    'permissions__menu_id': 2
}, {
    'permissions__url': '/customer/add/',
    'permissions__title': '添加客户',
    'permissions__menu__title': None,
    'permissions__menu__icon': None,
    'permissions__menu_id': None
}, {
    'permissions__url': '/customer/edit/(?P<cid>\\d+)/',
    'permissions__title': '编辑客户',
    'permissions__menu__title': None,
    'permissions__menu__icon': None,
    'permissions__menu_id': None
}, {
    'permissions__url': '/customer/del/(?P<cid>\\d+)/',
    'permissions__title': '删除客户',
    'permissions__menu__title': None,
    'permissions__menu__icon': None,
    'permissions__menu_id': None
}, {
    'permissions__url': '/payment/list/',
    'permissions__title': '缴费列表',
    'permissions__menu__title': '财务管理',
    'permissions__menu__icon': 'fa-cny',
    'permissions__menu_id': 1
}, {
    'permissions__url': '/baoxiao/list/',
    'permissions__title': '报销列表',
    'permissions__menu__title': '财务管理',
    'permissions__menu__icon': 'fa-cny',
    'permissions__menu_id': 1
}, {
    'permissions__url': '/payment/add/',
    'permissions__title': '添加缴费',
    'permissions__menu__title': None,
    'permissions__menu__icon': None,
    'permissions__menu_id': None
}, {
    'permissions__url': '/payment/edit/(?P<pid>\\d+)/',
    'permissions__title': '编辑缴费',
    'permissions__menu__title': None,
    'permissions__menu__icon': None,
    'permissions__menu_id': None
}, {
    'permissions__url': '/payment/del/(?P<pid>\\d+)/',
    'permissions__title': '删除缴费',
    'permissions__menu__title': None,
    'permissions__menu__icon': None,
    'permissions__menu_id': None
}]

ret = {}

for i in data:
    menu_id = i.get('permissions__menu_id')
    if not menu_id:
        continue

    if menu_id not in ret:
        ret[menu_id] = {
            'title': i.get('permissions__menu__title'),
            'icon': i.get('permissions__menu__icon'),
            'children' : [
                {'title':i.get('permissions__title'),'url':i.get('permissions__url')}
            ]
        }
    else:
        ret[menu_id]['children'].append( {'title':i.get('permissions__title'),'url':i.get('permissions__url')})


print(ret)

"""

{   
   1 : {
        'title' : '财务管理',
        'icon' : 'fa-cny',
        'children' :  [ 
            { 'title':'缴费列表' ,'url':'/payment/list/'},
            { 'title':'报销列表' ,'url':'/baoxiao/list/'},
         ]
    
    } ,
    2 : {
        'title' : '客户管理',
        'icon' : 'fa-user-o',
        'children' :  [ 
            { 'title':'客户列表' ,'url':'/customer/list/'},
         ]
    } ,
}
"""
