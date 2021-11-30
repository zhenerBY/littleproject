from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class AdvUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        pass


class AnimalImage(models.Model):
    class AnimalType(models.TextChoices):
        CAT = 'CAT', _('Cat')
        DOG = 'DOG', _('Dog')

    animal_type = models.CharField(max_length=3, choices=AnimalType.choices, default=AnimalType.CAT)
    pic_url = models.URLField(max_length=500)
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name=_('User'), related_name='Animal')
    file_type = models.CharField(max_length=10, default='jpg')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_('Created'))

    def __str__(self):
        return f'Image - {self.id} : {self.animal_type}'

    class Meta:
        ordering = ('created_at',)
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

