# image-resolution
The goal of this project is to build a smart solution that will allow enlarging while preserving high fidelity.

# gathering data
* For the purpose of working with high definition images, we gathered data from flickr website.
* In order to showcase the importance of insuring invariance to small image transformations while preserving high definition, and while this problem remains unsolved yet, we gatherd data using our script gather_labeled_flickr_img.py, every original image was resized to 224x224 and 64x64.
* The key words used are 'wild animal' and 'human portrait'
* By the end we got a 2 folders 'wild animal' and 'human portrait', each is divided into 2 other folders based on their size. Alonside with the images, we also labeled the data and stored in a pickle ordered dictionary.
