from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    # Define new fieldsets to include the 'name' field
    fieldsets = (
        (_('Personal info'), {'fields': ('name',)}), 
        (None, {'fields': ('phone', 'password')}),
         # Add 'name' field here
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    # Update add_fieldsets to include 'name' field for creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','phone',  'password1', 'password2'),  # Include 'name' here
        }),
    )
    # Update list_display to include 'name' to show it in the user list
    list_display = ('phone', 'name', 'is_staff')  # Add 'name' to list display
    # Allow searching by 'name' as well
    search_fields = ('phone', 'name')  # Add 'name' to search fields
    # Keep ordering by phone; adjust if you want 'name' to affect ordering
    ordering = ('phone',)

# Register the updated admin configuration
admin.site.register(CustomUser, UserAdmin)
