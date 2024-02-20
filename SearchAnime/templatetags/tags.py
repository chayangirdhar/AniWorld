from django import template

register = template.Library()

@register.filter
def Dsplit(value, arg):
    return value.split(arg)

