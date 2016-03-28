from __future__ import unicode_literals
from django.db import models
from django.core.files import File
import urllib, os

class Layout(models.Model): 
		image = models.ImageField(null = True, blank = True)
		original_image = models.ImageField(null = True, blank = True)
		name = models.CharField('name', max_length = 100, primary_key = True, default = "something")

		#causes admin page to display name instead of 'layout object'
		def __unicode__(self):
			return self.name

		def __str__(self): 
			return self.name 

