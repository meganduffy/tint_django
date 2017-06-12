from django import template

register = template.Library()


@register.filter
def individual_total_time(details):
    pass
