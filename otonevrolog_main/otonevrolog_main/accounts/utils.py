from django.contrib.auth.models import Group, User

from otonevrolog_main.accounts.models import CustomUser


def get_current_user(pk):
    return CustomUser.objects.get(pk=pk)


def get_doctor_administrators(pk):
    doctor_administrator_group = Group.objects.filter(name__in=['Doctor Administrator', 'Doctor Staff'])
    doctor_administrators = CustomUser.objects.filter(groups__in=doctor_administrator_group, pk=pk).distinct()
    return doctor_administrators
