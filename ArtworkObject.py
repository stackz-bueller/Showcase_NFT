from PIL import Image
from io import BytesIO
import requests

# Custom Class Built for Artwork in Collection
class Artwork():
    def __init__(self, items):
        self.Token = items['asset_contract']['name']
        self.TokenID = items['token_id']
        self.Name = items['name']
        self.Descrip = items['description']
        self.ImageURL = items['image_original_url']

    def to_string(self):
        print('Token: {}\tToken ID: {}\nName: {}\nDescription: {}\nImage URL: {}\n\n'.format(self.Token,
                                    self.TokenID,
                                    self.Name,
                                    self.Descrip,
                                    self.ImageURL))


    def __getitem__(self, index):
        result = self.text[index].upper()
        return result

    def __str__(self):
        return self

    def get_image(self):
        response = requests.get(self.ImageURL)
        img = Image.open(BytesIO(response.content))
        return img

    def get_image_source(self):
        filename = ImageURL.split('/')[-1]
        return urllib.request.urlretrieve(self.ImageURL,filename)
