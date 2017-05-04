from PIL import Image

class PixelSort:

    def __init__(self, image):
        self.image = Image.open(image).convert('RGBA')
        self.width = self.image.width
        self.height = self.image.height
        self.pixels = list(self.image.getdata())

        # 0 - black
        # 1 - brightness
        # 2 - white
        self.sortMethod = 1

    def sort(self):
        #iterate over columns
        # number of columns = len(self.pixels) / self.width
        self.sortColumns()
        #iterate over rows
        # number of rows = len(self.pixels) / self.height
        self.sortRows()
        #save new image
        print(len(self.pixels)/self.height)

    def sortColumns(self):
        column = 0
        index = 0
        # len(self.width)
        while column < self.width:
            self.sortColumn(column)
            column+=1

    def sortColumn(self, startIndex):
        # current column
        x = startIndex

        # where to start sorting
        y = 0

        # where to stop sorting
        yEnd = 0

        while yEnd < self.height:
            if self.sortMethod == 0:
                y = getFirstPixelNotBlackY(x, y)
                yEnd = getNextBlackPixelY(x, y)
                break
            elif self.sortMethod == 1:
                y = getFirstBrightPixelY(x, y)
                yEnd = getNextDarkPixelY(x, y)
                break
            elif self.sortMethod == 2:
                y = getFirstPixelNotWhiteY(x, y)
                yEnd = getNextWhitePixelY(x, y)
                break
            else:
                break

            if y < 0:
                break
            
            sortLength = yEnd - y
            pixelsInColumn = []
            
            for i in range(0, sortLength):
                pixelsInColumn.append(self.pixels[x + (y+i) * self.width])
            
            sortedPixels = sorted(pixelsInColumn)

            for i in range(0, sortLength):
                self.pixels[x + (y+i) * self.width] = sortedPixels[i]

            y = yEnd+1


    def sortRows(self):
        return

    # 0 - black
    # 1 - brightness
    # 2 - white
    def pixelSortImage(self, sortingMethod=1):
        self.sort()
        print('Pixel Sorting complete!')