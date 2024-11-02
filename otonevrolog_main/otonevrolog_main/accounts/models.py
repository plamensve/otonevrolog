from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    sex = models.CharField(max_length=5)
    # TODO: Тук мога да разширя модела за регистрация на потребител
