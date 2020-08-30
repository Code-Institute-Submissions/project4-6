from django.db import models

# Create your models here.


class Cuisine(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    location = models.ForeignKey(
        'Location', null=True, blank=True, on_delete=models.SET_NULL)
    cuisine = models.ForeignKey(
        'Cuisine', null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
