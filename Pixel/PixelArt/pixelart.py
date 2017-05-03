from PIL import Image

class PixelArt:

    def __init__(self, image):
        self.image = image

    def RGBtoHSL(self, color):
        r = color[0]
        g = color[1]
        b = color[2]

    def HSLtoRGB(self, color):
        h = color[0]
        s = color[1]
        l = color[2]

    