from atexit import register
from django import template
from core.models import *

register = template.Library()

@register.simple_tag()
def get_forms():
    forms = Forms.objects.all()
    return forms