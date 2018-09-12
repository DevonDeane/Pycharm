import random
import urllib.request

def dload_Web_Images(url):
    name = random.randrange(1, 500)
    fileName = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fileName)  # ->download this "url"(img), save it as "fileName" on this pc


dload_Web_Images("http://img09.deviantart.net/114f/i/2005/207/a/7/be_free_by_celsojunior.jpg")
