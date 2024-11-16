from django.contrib import admin
from django.contrib.auth import get_user_model
from unfold.admin import ModelAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    ordering = ('-date_joined',)
    fields = ('username', 'email', 'is_active', 'is_staff', 'date_joined')
