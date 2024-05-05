from django.db import models

# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.language

