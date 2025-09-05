from django.db import models
from django.core.validators import FileExtensionValidator
class recipe_model(models.Model):
    recipe_name=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(upload_to="recipes/")


