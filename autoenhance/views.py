from PIL import Image
import requests 
from PIL import ImageEnhance
from StringIO import StringIO
import urllib
import operator 
import os 
####################################
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Layout
from django_ajax.decorators import ajax
from django.conf import settings 
from django.core.files import File
from django.http import JsonResponse

IMAGE_NAME = "key"

def autoenhance(im): 
  	h = im.convert("L").histogram()
  	lut = []
  	for b in range(0, len(h), 256):
    		# step size
    		step = reduce(operator.add, h[b:b+256]) / 255
    		# create equalization lookup table
    		n = 0
    		for i in range(256):
      			lut.append(n / step)
      			n = n + h[i+b]
  	    # map image through lookup table
 		return im.point(lut*im.layers)

def index(request):
    if request.is_ajax(): 
        try:
            import json
        except ImportError:
            import simplejson
        print "Ajax"

        layout = Layout.objects.get(name=IMAGE_NAME)

        if request.POST.get('undo') == "true": 
            layout.image = layout.original_image 
            layout.save() 
            response_data = {
                'message' : 'success', 
                'data' : layout.original_image.url 
            }
            return HttpResponse(json.dumps(response_data))        
        else: 
            img = Image.open(layout.image)
            processedImage = autoenhance(img)
            print "Trying to save"
            print layout.image.url 
            processedImage.save("django_images/image.jpg")
            layout.image.save(os.path.basename("image.jpg"), File(open("django_images/image.jpg")))
            layout.save() 
            print layout.image.url 
            response_data = {}
            response_data['message'] = "success" 
            response_data['data'] = layout.image.url 
            return HttpResponse(json.dumps(response_data))

    #when page is first loaded 
    else: 
        url = "http://www.nasa.gov/sites/default/files/thumbnails/image/iss043e241982.jpg"
        
        #copy image to upload to folder 
        result = urllib.urlretrieve(url) 

        #saving data to model 
        layout = Layout() 
        layout.image.save(os.path.basename("image.jpg"), File(open(result[0])))
        layout.original_image.save(os.path.basename("image.jpg"), File(open(result[0])))
        layout.name = IMAGE_NAME
        layout.save() 

        #have template display what is in layout  
        context = {
          'data' : layout, 
        }

    template = loader.get_template('autoenhance/index.html')
    return HttpResponse(template.render(context, request))




