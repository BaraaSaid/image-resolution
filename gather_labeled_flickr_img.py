import flickrapi
import urllib
from PIL import Image
import sys
import urllib.request
import os
import requests
from urllib.parse import urlparse
from collections import OrderedDict
import pickle

# Flickr api access key 
flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)

WRK_DIR = '/home/jupyter/ImagesResolution/A'
DATA_DIR = os.path.join(WRK_DIR, 'Data')
HUMAN_DIR = os.path.join(DATA_DIR, 'human portrait')
DATA_224_DIR = os.path.join(HUMAN_DIR,'I224')
DATA_64_DIR = os.path.join(HUMAN_DIR,'I64')

keyword = sys.argv[1]
size = sys.argv[2]
print(size)
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
labels = []
photo_names = []                      
#sizes = [224, 64]
if size == '224':
    image_folder = DATA_224_DIR
    print(image_folder)
elif size == '64':
    image_folder = DATA_64_DIR
    print(image_folder)
    
image_dict = OrderedDict({'photo_names':photo_names, 'labels':labels})
    
for i in range(len(urls)):
    
    print(urls[i])
    image_name = keyword.replace(' ','_')+'_'+str(i)
    print(image_name)
    photo_name = image_name +'.jpg'
    print(photo_name)
    
    urllib.request.urlretrieve(urls[i], photo_name)
    
    photo_path = os.path.join(image_folder, photo_name)
    print(photo_path)
    
    image = Image.open(photo_name)
    size = int(size)
    image = image.resize((size, size), Image.ANTIALIAS)
    image.save(photo_path)
                         
    photo_names.append(photo_name)
    labels.append(keyword)
    image_dict = OrderedDict({'photo_names':photo_names, 'labels':labels})
    image_dict_path = os.path.join(image_folder, 'image_dict.pickle' )
    
    with open(image_dict_path, 'wb') as handle:
        pickle.dump(image_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
