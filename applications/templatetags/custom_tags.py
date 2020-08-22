from django import template

register = template.Library()

@register.filter
def remaining_days(application):
	print('filter')
	return '1';
