from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Product(models.Model):
    description = models.CharField(max_length=200, verbose_name=("description"))
    owner = models.ForeignKey('auth.User', related_name='owner', on_delete=models.CASCADE, default=False)
    name = models.CharField(max_length=50, blank=True,null=True, verbose_name=("name"))
    price = models.IntegerField(null=True, blank=True, verbose_name=("price"))
