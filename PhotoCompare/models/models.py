# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=100)
    content = models.ImageField(upload_to='photo/%Y/%m/%d')
    favorNum = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)
