from django.contrib import admin
from django.contrib.auth import get_user_model
from unfold.admin import ModelAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(ModelAdmin):
    pass
