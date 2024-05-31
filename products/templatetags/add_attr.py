from django import template
register = template.Library()


@register.filter(name="add_attr")
def add_attr(field, css):
    attrs = {}
    classe, value = css.split(':')
    attrs[classe] = value
    return field.as_widget(attrs=attrs)
