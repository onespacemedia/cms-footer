from django.contrib import admin
from reversion.admin import VersionAdmin
from suit.admin import SortableModelAdmin, SortableStackedInline

from .models import Footer, FooterLink, FooterLinkGroup


class FooterLinkInline(SortableStackedInline):
    model = FooterLink
    extra = 0


@admin.register(FooterLinkGroup)
class FooterLinkGroupAdmin(VersionAdmin, SortableModelAdmin):
    inlines = [FooterLinkInline]
    list_display = ['link_text', 'link', 'page']


class FooterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Footer.objects.count()


admin.site.register(Footer, FooterAdmin)
