from django import template
# Create your views here.



register = template.Library()
@register.filter(name='replace_underscore')
def replace_underscore(value):
    return value.replace('_', ' ')