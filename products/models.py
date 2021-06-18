from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Menu(models.Model):
    menu_name = models.CharField(max_length=45)

class Categories(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    categories_name = models.CharField(max_length=45)

class Nutritions(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

class Products(models.Model):
    categories= models.ForeignKey(Categories, on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField
    nutrition = models.ForeignKey(Nutritions, on_delete=models.CASCADE)

class Images(models.Model):
    image_url = models.CharField(max_length=2000)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

class Allergy(models.Model):
    allergy_name =  models.CharField(max_length=45)

class Allergy_products(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)