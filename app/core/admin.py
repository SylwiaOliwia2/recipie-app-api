from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    # fieldsets makes layout changes in the forms on the “add” and “change” pages such as showing only a subset of available fields
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('presonal_info'), {'fields': ('name',)}),
        (('Permissions'),{'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(models.User, UserAdmin)
