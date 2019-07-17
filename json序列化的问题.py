import json

data = {
    1: {
        'url': '/customer/list/',
        'id': 1,
        'pid': None,
        'title': '客户列表'
    },
    2: {
        'url': '/customer/add/',
        'id': 2,
        'pid': 1,
        'title': '添加客户'
    },
    3: {
        'url': '/customer/edit/(?P<cid>\\d+)/',
        'id': 3,
        'pid': 1,
        'title': '编辑客户'
    },
    4: {
        'url': '/customer/del/(?P<cid>\\d+)/',
        'id': 4,
        'pid': 1,
        'title': '删除客户'
    },
    5: {
        'url': '/payment/list/',
        'id': 5,
        'pid': None,
        'title': '缴费列表'
    },
    6: {
        'url': '/payment/add/',
        'id': 6,
        'pid': 5,
        'title': '添加缴费'
    },
    7: {
        'url': '/payment/edit/(?P<pid>\\d+)/',
        'id': 7,
        'pid': 5,
        'title': '编辑缴费'
    },
    8: {
        'url': '/payment/del/(?P<pid>\\d+)/',
        'id': 8,
        'pid': 5,
        'title': '删除缴费'
    }
}

ret = json.dumps(data)

ret = json.loads(ret)
print(ret)

data = {'customer_list': {'url': '/customer/list/', 'id': 1, 'pid': None, 'pname': None, 'title': '客户列表'},
        'customer_add': {'url': '/customer/add/', 'id': 2, 'pid': 1, 'pname': 'customer_list', 'title': '添加客户'},
        'customer_edit': {'url': '/customer/edit/(?P<cid>\\d+)/', 'id': 3, 'pid': 1, 'pname': 'customer_list',
                          'title': '编辑客户'},
        'customer_del': {'url': '/customer/del/(?P<cid>\\d+)/', 'id': 4, 'pid': 1, 'pname': 'customer_list',
                         'title': '删除客户'},
        'payment_list': {'url': '/payment/list/', 'id': 5, 'pid': None, 'pname': None, 'title': '缴费列表'},
        'payment_add': {'url': '/payment/add/', 'id': 6, 'pid': 5, 'pname': 'payment_list', 'title': '添加缴费'},
        'payment_edit': {'url': '/payment/edit/(?P<pid>\\d+)/', 'id': 7, 'pid': 5, 'pname': 'payment_list',
                         'title': '编辑缴费'},
        'payment_del': {'url': '/payment/del/(?P<pid>\\d+)/', 'id': 8, 'pid': 5, 'pname': 'payment_list',
                        'title': '删除缴费'}}
