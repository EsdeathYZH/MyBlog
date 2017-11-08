# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','slug','publish_date')

admin.site.register(models.Post,PostAdmin)