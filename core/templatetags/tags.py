from atexit import register
from django import template
from core.models import *
import datetime


register = template.Library()

@register.simple_tag()
def get_forms():
    forms = Forms.objects.all()
    return forms


@register.filter(name='apiDate')
def apiDate(val):
    val = val[0:19]
    result = datetime.datetime.strptime(val, '%Y-%m-%dT%H:%M:%S').strftime('%d-%m-%Y  %H:%M')
    return result