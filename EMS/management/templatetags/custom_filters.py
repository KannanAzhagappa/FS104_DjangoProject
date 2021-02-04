from django import template

register = template.Library()


@register.filter('req_label')
def req_label(field):
    return field.field.widget.is_required


@register.filter('req_perms')
def req_perms(value, user):
    return user.has_perm(value)