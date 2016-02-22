from django import template

from ..models import Footer, FooterLinkGroup

register = template.Library()


@register.assignment_tag(takes_context=True)
def footer_link_groups(context):
    return FooterLinkGroup.objects.prefetch_related("children").all()


@register.assignment_tag()
def footer_content():
    try:
        return Footer.objects.all()[:1][0]
    except IndexError:
        return None
