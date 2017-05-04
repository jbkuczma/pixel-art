from PIL import Image, ImageEnhance
from .. import util

class PixelArt:

    def __init__(self, image):
        self.image = Image.open(image).convert('RGB')
        self.width = self.image.width
        self.height = self.image.height
        self.pixels = self.getPixels()

    def RGBtoHSL(self, color):
        r = color[0]
        g = color[1]
        b = color[2]
        print(color)

    def HSLtoRGB(self, color):
        h = color[0]
        s = color[1]
        l = color[2]

    def getPixels(self):
        return list(self.image.getdata())

    def saturateImage(self):
        converter = ImageEnhance.Color(self.image)
        self.image = converter.enhance(2.0)

    def reduceNumberOfColorsInPalette(self, numberOfColors):
        reduced = self.image.convert('P', palette=Image.ADAPTIVE, colors=numberOfColors)
        self.image = reduced

    def resizeImageWithPixel(self):
        # change
        resized = self.image.resize((75, 50), Image.ANTIALIAS)
        self.image = resized

    def resizeImageWithPercent(self, percent):
        # resize image back up to its original dimensions (or a percent of the desired dimensions)
        # since util.turnNumberIntoPercent() returns a float, we need to cast the new width/height to an int after multiplying so that image.resize will work
        width = int(self.width * util.turnNumberIntoPercent(percent))
        height = int(self.height * util.turnNumberIntoPercent(percent))
        resized = self.image.resize((width, height), Image.ANTIALIAS)
        self.image = resized

    def save(self, filename):
        self.image.save(filename)

    def turnImageIntoPixelArt(self, numberOfColorsInPalette, resizePercent, outputFilename):
        self.saturateImage()
        self.reduceNumberOfColorsInPalette(numberOfColorsInPalette)
        self.resizeImageWithPixel()
        self.resizeImageWithPercent(resizePercent)
        self.save(outputFilename)
        print('Pixel Art complete!')
        

    