from django import template

register = template.Library()


@register.filter(name="option_label")
def option_label(value):
    # A, B, C, D for 1, 2, 3, 4 respectively
    return chr(64 + value)


@register.filter
def divfloat(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0


@register.filter
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except ValueError:
        return 0
