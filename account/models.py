from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(AbstractUser):
    rating = models.PositiveIntegerField(default=0)
    week_rating = models.PositiveIntegerField(default=0)
    lesson_number = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='users')
    completed_lessons = ArrayField(models.IntegerField(), blank=True, default=list)
    strike = models.PositiveIntegerField(blank=True, default=0)
    strike_status = models.BooleanField(blank=True, default=False)
    last_lesson_date = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    # groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    # user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_user_permissions')

    @property
    def get_image(self):
        return self.image.url
    def __str__(self):
        return self.username
