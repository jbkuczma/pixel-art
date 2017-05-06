from Pixel import PixelArt
from Pixel import PixelSort


# x = PixelArt('images/chicago_test.png')
# x.turnImageIntoPixelArt('tester.png')

# x = PixelArt('images/5.jpg')
# x.turnImageIntoPixelArt('tester2.png', numberOfColorsInPalette=20)

x = PixelSort('images/5.jpg')
x.pixelSortImage('o7.png', sortingMethod=1)

