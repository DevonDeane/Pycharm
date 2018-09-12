import random
import urllib.request

def dload_Web_Images(url):
    name = random.randrange(1, 500)
    fileName = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fileName)  # ->download this "url"(img), save it as "fileName" on this pc


dload_Web_Images("https://s-media-cache-ak0.pinimg.com/originals/23/c6/d0/23c6d00821cb35e73310d1c91be95626.jpg")
