# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=200)
	slug=models.CharField(max_length=200)
	body=models.TextField()
	publish_date=models.DateTimeField(default=timezone.now)

	class Meta:
		ordering=('-publish_date',)

	def __unicode__(self):
		return self.title