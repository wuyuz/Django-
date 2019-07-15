from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=32, verbose_name='菜单名')
    icon = models.CharField('图标', max_length=32) # 它是不需要url
    
    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField('用户名',max_length=12)
    pwd = models.CharField('密码',max_length=12)
    role = models.ManyToManyField('Role', related_name='users',verbose_name='用户拥有角色',blank=True)
    
    def __str__(self):
        return self.username

class Permission(models.Model):
    url = models.CharField('url地址',max_length=32)
    title = models.CharField('标题',max_length=32)
    is_menu = models.BooleanField(default=False,verbose_name='是否是菜单')
    #icon = models.CharField('图标', max_length=32)
    menu = models.ForeignKey('Menu',blank=True,null=True) # 有些权限不用再菜单下，有menu_id的url是二级菜单，没有则是普通权限
    
    def __str__(self):
        return self.title


class Role(models.Model):
    name = models.CharField(max_length=12)
    permission = models.ManyToManyField('Permission', related_name='roles',verbose_name='角色所拥有的权限',blank=True)
    
    def __str__(self):
        return self.name

