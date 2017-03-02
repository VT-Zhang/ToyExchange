from __future__ import unicode_literals

from django.db import models
from ..login.models import User
from PIL import Image

class Toy(models.Model):
    name = models.CharField(max_length=45)
    msrp = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    condition = models.CharField(max_length=45)
    text = models.TextField(max_length=1000)
    zipcode = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='useruser')

class Image(models.Model):
    img = models.ImageField(upload_to='photo')
    toy = models.ForeignKey(Toy, related_name='toytoy')
