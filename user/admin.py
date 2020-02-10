from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# #####
from user.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff',)
    ieldsets = (
        (None, {'fields': ('email', 'password')}),
        # (_('Personal Info'),{'fields': ('id', )}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser',)
            }
        ),
        (_('Important Dates'), {
            'fields': ('last_login', )
        }),
    )
    add_fieldsets = (
        (None, {'classes': ('wide'),
                'fields': ('email',
                           'password1',
                           'password2')
                }),
    )
    search_fields = ('email',)
    ordering = ('email',)


# unregistering Group
admin.site.unregister(Group)

# registering custom Models
admin.site.register(User, UserAdmin)
