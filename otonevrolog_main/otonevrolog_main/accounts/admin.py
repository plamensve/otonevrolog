from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from otonevrolog_main.accounts.forms import CustomCreateUserForm
from otonevrolog_main.accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomCreateUserForm
    form = CustomCreateUserForm
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
