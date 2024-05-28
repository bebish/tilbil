from django.db import models

# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='languages_images',default='default_lesson.avif')

    @property
    def get_image(self):
        return self.image.url

    def __str__(self) -> str:
        return self.language

class Level(models.Model):
    title = models.CharField(max_length=50)
    language = models.ForeignKey(Language,on_delete=models.CASCADE,related_name='levels')
    description = models.TextField()
    image = models.ImageField(upload_to='levels_images')

    @property
    def get_image(self):
        return self.image.url

    def __str__(self) -> str:
        return self.title
    
