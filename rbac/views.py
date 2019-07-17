from django.shortcuts import render, redirect, reverse
from rbac import models
from rbac.forms import RoleForm, MenuForm


def role_list(request):
    all_roles = models.Role.objects.all()
    return render(request, 'rbac/role_list.html', {'all_roles': all_roles})


def role_change(request, pk=None):
    obj = models.Role.objects.filter(pk=pk).first()
    form_obj = RoleForm(instance=obj)
    if request.method == 'POST':
        form_obj = RoleForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('role_list'))
    return render(request, 'form.html', {'form_obj': form_obj})

from django.db.models import Q

def menu_list(request):
    mid = request.GET.get('mid')

    all_menus = models.Menu.objects.all()
    if not mid:
        all_permissions = models.Permission.objects.all()
    else:
        all_permissions = models.Permission.objects.filter(Q(menu_id=mid)|Q(parent__menu_id=mid))


    """
    { id : {
                children： [ {}  {} ]
         } 
    }

    """
    permission_dict = {}

    for i in all_permissions.values('id','title','url','name','menu_id','menu__title','parent_id'):
        menu_id = i.get('menu_id')
        if menu_id:
            permission_dict[i['id']] = i
            i['children'] = []

    for i in all_permissions.values('id','title','url','name','menu_id','menu__title','parent_id'):
        pid = i.get('parent_id')
        if pid:
            permission_dict[pid]['children'].append(i)

    print(permission_dict)


    return render(request, 'rbac/menu_list.html', {
        'all_menus': all_menus,
        'all_permissions': permission_dict.values(),
        'mid': mid
    })


def menu_change(request, pk=None):
    obj = models.Menu.objects.filter(pk=pk).first()
    form_obj = MenuForm(instance=obj)
    if request.method == 'POST':
        form_obj = MenuForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('menu_list'))
    return render(request, 'form.html', {'form_obj': form_obj})
