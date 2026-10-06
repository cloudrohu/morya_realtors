from django import template

register = template.Library()

@register.filter(name='in_lakh_crore')
def in_lakh_crore(value):
    """
    Converts raw integer price (e.g. 5000000) into ₹ 50 Lac or ₹ 1.25 Cr format.
    """
    if not value or value == 0:
        return "Price on Request"

    try:
        val = float(value)
    except (ValueError, TypeError):
        return value

    if val >= 10000000:
        cr = val / 10000000
        # 1.20 Cr -> 1.2 Cr, 1.00 Cr -> 1 Cr
        formatted = f"{cr:.2f}".rstrip('0').rstrip('.')
        return f"₹ {formatted} Cr"
    elif val >= 100000:
        lakh = val / 100000
        formatted = f"{lakh:.2f}".rstrip('0').rstrip('.')
        return f"₹ {formatted} Lac"
    else:
        return f"₹ {int(val):,}"