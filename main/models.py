from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        pass
