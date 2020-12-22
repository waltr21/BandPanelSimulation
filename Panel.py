import time
import random

class Panel:
    def __init__(self):
        self.width = 42
        self.height = 35
        self.size = self.width * self.height
        self.grid = None
        self.initGrid()
        self.brightness = 1.00

    def initGrid(self):
        self.grid = [[0 for i in range(self.height)] for j in range(self.width)]

    def getColor(self, col, brightness=-1):
        b = 0
        if (brightness < 0):
            b = self.brightness
        else:
            b = brightness
        return color(col[0] * b, col[1] * b, col[2] * b)

    def setBackground(self, col):
        #self.pixels.fill(self.getColor(col))
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y] = self.getColor(col)

    def setPixel(self, x, y, col, brightness=-1):
        self.grid[int(x)][int(y)] = self.getColor(col, brightness)

    def show(self):
        xIncr = 15
        yIncr = 15
        eSize = 10
        xStart = (width - ((xIncr - eSize) + eSize) * self.width) / 2
        yStart = (height - ((yIncr - eSize) + eSize) * self.height) / 2


        xPos = xStart
        yPos = yStart
        ellipseMode(CENTER)
        for y in range(self.height):
            for x in range(self.width):
                c = self.grid[x][y]
                fill(c)
                ellipse(xPos,yPos,eSize,eSize)
                xPos += xIncr
            xPos = xStart
            yPos += yIncr

    def getMillis(self):
        return int(round(time.time() * 1000))

    def sideScroll(self):
        while (i < self.width):
            while(j < self.height):
               self.pixels[self.grid[i][j]] = self.getColor(100,0,0, brightness)
               i += 1
               j+= 1
            