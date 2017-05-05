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

        self.blackValue = -16000000
        self.brightnessValue = 60
        self.whiteValue = -13000000

    def sort(self):
        #iterate over columns
        # number of columns = len(self.pixels) / self.width
        self.sortColumns()
        #iterate over rows
        # number of rows = len(self.pixels) / self.height
        self.sortRows()
        #save new image
        print(len(self.pixels)/self.height)

    ### Column ###
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
                y = self.getFirstPixelNotBlackY(x, y)
                yEnd = self.getNextBlackPixelY(x, y)
                break
            elif self.sortMethod == 1:
                y = self.getFirstBrightPixelY(x, y)
                yEnd = self.getNextDarkPixelY(x, y)
                break
            elif self.sortMethod == 2:
                y = self.getFirstPixelNotWhiteY(x, y)
                yEnd = self.getNextWhitePixelY(x, y)
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
    
    def getFirstPixelNotBlackY(self, x, y):
        if y < self.height:
            while self.pixels[x + y * self.width] < self.blackValue:
               y+=1
               if y >= self.height:
                   return - 1
        return y 

    def getNextBlackPixelY(self, x, y):
        y+=1
        if y < self.height:
            while self.pixels[x + y * self.width] > self.blackValue:
                y+=1
                if y >= self.height:
                    return self.height - 1
        return y-1

    def getFirstBrightPixelY(self, x, y):
        if y < self.height:
            while self.getBrightness(self.pixels[x + y * self.width]) < self.brightnessValue:
                y+=1
                if y >= self.height:
                    return -1
        return y

    def getNextDarkPixelY(self, x, y):
        y+=1
        if y < self.height:
            while self.getBrightness(self.pixels[x + y * self.width]) > self.brightnessValue:
                y+=1
                if y >= self.height:
                    return self.height - 1
        return y-1

    def getFirstPixelNotWhiteY(self, x, y):
        if y < self.height:
            while self.pixels[x + y * self.width] > self.whiteValue:
                y+=1
                if y >= self.height:
                    return -1
        return y

    def getNextWhitePixelY(self, x, y):
        y+=1
        if y < self.height:
            while self.pixels[x + y * self.width] < self.whiteValue:
                y+=1
                if y >= self.height:
                    return self.height-1
        return y-1
    ### End of Column section ###

    ### Row ###
    def sortRows(self):
        row = 0
        index = 0
        # len(self.width)
        while row < self.height:
            self.sortRow(row)
            row+=1
    
    def sortRow(self, startIndex):
        # current row
        y = startIndex

        # where to start
        x = 0

        # where to stop
        xEnd = 0

        while xEnd < self.width-1:
            if self.sortMethod == 0:
                x = self.getFirstPixelNotBlackX(x, y)
                xEnd = self.getNextBlackPixelX(x, y)
                break
            elif self.sortMethod == 1:
                x = self.getFirstBrightPixelX(x, y)
                xEnd = self.getNextDarkPixelX(x, y)
                break
            elif self.sortMethod == 2:
                x = self.getFirstPixelNotWhiteX(x, y)
                xEnd = self.getNextWhitePixelX(x, y)
                break
            else:
                break
            
            if x < 0:
                break
            
            sortLength = xEnd - x
            pixelsInRow = []

            for i in range(0, sortLength):
                pixelsInRow.append(self.pixels[x + i + y * self.width])
            
            pixelsInRow = sorted(pixelsInRow)

            for i in range(0, sortLength):
                self.pixels[x + i + y * self.width] = pixelsInRow[i]
            
            x = xEnd+1


    ### End of Row section ###


    
    # extract brightness from a color
    # formula: https://en.wikipedia.org/wiki/Relative_luminance
    def getBrightness(self, pixel):
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        return (r * 0.2126) + (g * 0.7152) + (b * 0.0722)

    def pixelSortImage(self, sortingMethod=1):
        # set the sorting method
        self.sortMethod = sortingMethod
        self.sort()
        print('Pixel Sorting complete!')