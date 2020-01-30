import flickrapi
import urllib
from PIL import Image
import sys
import urllib.request
import os
import requests
from urllib.parse import urlparse


# Flickr api access key 
flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)

WRK_DIR = '/home/jupyter/ImagesResolution'

keyword = sys.argv[1]

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=100,           # may be you can try different numbers..
                     sort='relevance')
urls = []
for i, photo in enumerate(photos):
    print (i)
    url = photo.get('url_c')
    if urlparse(url).scheme:
        urls.append(url)
     # get 1000 urls
    if i > 1000:
        break
    
# Download image from the url and save it to resized or original folder
#to do : resize the image respcting the coeff between the width and the height

sizes = [310, 256, 200, 128, 64, 48, 32, 16]
for i in range(len(urls)):
    print(urls[i])
    image_name = keyword.replace(' ','_')+'_'+str(i)
    print(image_name)
    photo_name = image_name +'.jpg'
    print(photo_name)
    
    urllib.request.urlretrieve(urls[i], photo_name)
    image_folder = os.path.join(WRK_DIR, image_name)
    print(image_folder)
    original_image_folder = os.path.join(image_folder, 'original')
    print(original_image_folder)
    if not os.path.exists(original_image_folder):
        os.makedirs(original_image_folder)
        photo_path = os.path.join(original_image_folder, photo_name)
        print(photo_path)
        image = Image.open(photo_name)
        image.save(photo_path)
        resized_image_folder = os.path.join(image_folder, 'resized')
        print(resized_image_folder)
        if not os.path.exists(resized_image_folder):
            os.makedirs(resized_image_folder)
            for size in sizes:
                resized_image_name = image_name+'_size_'+str(size)
                print(resized_image_name)
                photo_resized_name = resized_image_name +'.jpg'
                print(photo_resized_name)
                photo_resized_path = os.path.join(resized_image_folder, photo_resized_name)
                print(photo_resized_path)
                image = Image.open(photo_name)
                image = image.resize((size, size), Image.ANTIALIAS)
                image.save(photo_resized_path)
