from django.contrib import admin
from django.contrib.auth import get_user_model
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'group', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'groups'),
        }),
    )

    def group(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    group.short_description = 'Group'
