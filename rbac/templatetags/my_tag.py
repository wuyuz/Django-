from django import template
from django.conf import settings
register = template.Library()
import re

@register.inclusion_tag('menu.html')
def menu(request):
    
    menu_dict = request.session.get(settings.MENU_SESSION_KEY)

    return {'menu_list':menu_dict.values()}