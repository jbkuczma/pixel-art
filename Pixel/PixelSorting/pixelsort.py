from PIL import Image

class PixelSort:

    def __init__(self, image):
        self.image = Image.open(image).convert('RGBA')
        self.width = self.image.width
        self.height = self.image.height
        self.pixels = self.image.load()