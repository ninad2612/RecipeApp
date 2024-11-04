from django.db import models
import os

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipeimg')
    recipe_view_count = models.IntegerField(default=0)

    def delete(self, *args, **kwargs):
        # Delete the image file from the filesystem if it exists
        if self.recipe_image and os.path.isfile(self.recipe_image.path):
            os.remove(self.recipe_image.path)
        # Call the superclass delete method to delete the record from the database
        super().delete(*args, **kwargs)

