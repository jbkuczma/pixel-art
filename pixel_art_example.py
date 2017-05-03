from Pixel import PixelArt


x = PixelArt('images/chicago_test.png')
x.saturateImage()
x.reduceNumberOfColorsInPalette(25)
x.resizeImageWithPixel()
x.resizeImageWithPercent(100)
x.save('tester.png')
print('good')
