import cv2, requests
from urllib.request import Request, urlopen
import numpy as np

# Gets Collection at Address by building parameter for API
def get_collection(owner_address):
    url = 'https://api.opensea.io/api/v1/assets'
    querystring = {'owner':owner_address,'limit':'300'}
    response = requests.request('GET', url, params=querystring).json()
    return response

def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urlopen(req)
        image = np.asarray(bytearray(resp.read()), dtype='uint8')
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        # return the image
        return image

def print_wallet(wallet):
    if(art_wallet != None):
        print('\nThis collection has {} pieces of Artwork\n\n'.format(len(art_wallet)))
        for piece in art_wallet:
            piece.to_string()

    else:
        print('This address has no Art')

def random_art(wallet):
    rando = random.choice(wallet)
    return rando
