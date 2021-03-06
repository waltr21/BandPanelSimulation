import random

class Square:
    def __init__(self, w, h, c, p):
        # Top left x/y coordinates of the square.
        self.x = random.randint(0,p.width)
        self.y = random.randint(0,p.height)

        # Dimensions of the square
        self.width = w
        self.height = h

        # Reference to the panel object
        self.panel = p

        # Color of square
        self.col = c

        # Movement
        self.velocity = (random.uniform(1.0,2.0), random.uniform(1.0,2.0))

        #self.brightness = random.random()
        self.brightness = 1.0
        self.bAdjust = 1.0

    def update(self):
        # Move by x and y from velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        #self.brightness += self.bAdjust
        self.bound()
        self.show()

    def bound(self):
        if (self.x < 0):
            self.x = 0
            self.velocity = (self.velocity[0] * -1, self.velocity[1])
        if (self.x + self.width > self.panel.width - 1):
            self.x = self.panel.width - self.width
            self.velocity = (self.velocity[0] * -1, self.velocity[1])
        if (self.y < 0):
            self.y = 0
            self.velocity = (self.velocity[0], self.velocity[1] * -1)
        if (self.y + self.height > self.panel.height - 1):
            self.y = self.panel.height - self.height
            self.velocity = (self.velocity[0], self.velocity[1] * -1)
        if (self.brightness < 0):
            self.brightness = 0
            self.bAdjust *= -1
        if (self.brightness > 1.0):
            self.brightness = 1.0
            self.bAdjust *= -1

    def show(self):
        roundX = int(self.x)
        roundY = int(self.y)
        for curX in range(roundX, roundX + self.width):
            for curY in range(roundY, roundY + self.height):
                self.panel.setPixel(curX, curY, self.col, self.brightness)

class BouncingSquares():
    def __init__(self, w, h, numSquares, p):
        self.squares = []
        self.panelRef = p
        #col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        for i in range(numSquares):
            col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.squares.append(Square(w,h,col,p))

    def update(self):
        self.panelRef.setBackground((0,0,0))
        for i in self.squares:
            i.update()
