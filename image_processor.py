import cv2
from urllib import request

class ImageProcessor():

    def __init__(self):
        self.IMAGE_SIZE = 28
    
    def imageGenerator(self, imagedata):
        with request.urlopen(imagedata.decode('ASCII')) as response:
            data = response.read()
        
        with open("image.png", "wb") as f:
            f.write(data)

    def imageProcessor(self):
        img_array = cv2.imread(".\image.png", cv2.IMREAD_GRAYSCALE)
        img_array = 255.0 - img_array
        new_array = cv2.resize(img_array, (self.IMAGE_SIZE, self.IMAGE_SIZE))
        new_array = new_array.reshape(1, self.IMAGE_SIZE, self.IMAGE_SIZE)
        return new_array

