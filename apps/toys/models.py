from __future__ import unicode_literals

from django.db import models
from ..login.models import User

class Toy(models.Model):
    name = models.CharField(max_length=45)
    msrp = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField()
    category = models.IntegerField()
    condition = models.IntegerField()
    img = models.ImageField(upload_to='documents/')
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='useruser')
