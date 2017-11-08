# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Post
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import render
# Create your views here.

def homepage(request):
	template=get_template("index.html")
	now=datetime.now()
	posts=Post.objects.all()
	html = template.render(locals())
	return HttpResponse(html)