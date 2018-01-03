# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Photo


# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'favorNum',)
    fields = ('name', 'content')


admin.site.register(Photo, PhotoAdmin)
