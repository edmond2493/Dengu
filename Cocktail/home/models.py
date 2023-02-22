from django.db import models

# Create your models here.

class Tool(models.Model):
    tool_id = models.AutoField(primary_key=True)
    tool_name = models.CharField(max_length=50)
    tool_image = models.ImageField(upload_to='static/media/tools')

    def __str__(self):
        return f'{self.tool_name}'


class Alcohol(models.Model):
    alcohol_id = models.AutoField(primary_key=True)
    alcohol_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.alcohol_name}'

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=100)
    recipe_alcohol = models.ManyToManyField(Alcohol)
    recipe_image1 = models.ImageField(upload_to='static/media/recipes')
    recipe_image2 = models.ImageField(upload_to='static/media/recipes')
    recipe_title = models.CharField(max_length=100)
    recipe_description = models.TextField(max_length=1000)
    recipe_ingredients = models.TextField(max_length=1000)
    recipe_steps = models.TextField(max_length=1000)
    recipe_tools = models.ManyToManyField(Tool)

    def __str__(self):
        return f'{self.recipe_name}'

class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=100)
    food_alcohol = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    food_image1 = models.ImageField(upload_to='static/media/food')
    food_image2 = models.ImageField(upload_to='static/media/food')
    food_title = models.CharField(max_length=100)
    food_description = models.TextField(max_length=1000)
    food_ingredients = models.TextField(max_length=1000)
    food_steps = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.food_name}'