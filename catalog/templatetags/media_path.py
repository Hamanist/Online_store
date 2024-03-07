from django import template

register = template.Library()


@register.filter()
def path_media(data):
    if data:
        return f'/media/{data}'
    return '#'
