from collections import OrderedDict

od = OrderedDict()
od['k2'] = 'v2'
od['k1'] = 'v1'
od['k3'] = 'v3'

data = {
    2: {'title': '客户管理', 'icon': 'fa-user-o', 'weight': 10, 'children': [{'title': '客户列表', 'url': '/customer/list/'}]},
    1: {'title': '财务管理', 'icon': 'fa-cny', 'weight': 100, 'children': [{'title': '缴费列表', 'url': '/payment/list/'}]}}

# ret = sorted([4, 5, 1, 2, 6],reverse=True)
# ret = sorted(data,reverse=True)
ret = sorted(data,key=lambda x:data[x]['weight'],reverse=True)
print(ret)

