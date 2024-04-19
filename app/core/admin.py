"""
Django Admin Customization
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# not used but good for future?
from django.utils.translation import gettext_lazy as _

from core import models


# changes to BaseUserAdmin
class UserAdmin(BaseUserAdmin):
    """Define admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    # customize fieldset class variable for fields
    # that exist and model or in PermissionsMixin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
