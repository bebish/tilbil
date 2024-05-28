from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    rating = models.PositiveIntegerField(default=0)
    lesson_number = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='users')

    # groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    # user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_user_permissions')

    @property
    def get_image(self):
        return self.image.url
    def __str__(self):
        return self.username