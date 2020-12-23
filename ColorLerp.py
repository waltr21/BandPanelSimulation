import random
class ColorLerp:
    def __init__(self, speed, p):
        #self.color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.color2 = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        #self.color1 = (255.0, 0.0, 0.0)
        #self.color2 = (255.0, 255.0, 0.0)
        self.curColor = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        self.panel = p
        self.speed = speed
    
    def lerp(self, a, b, c):
        res = (c * a) + ((1-c) * b)
        #print(str.format("a: {0}, b:{1}, c: {2}, res: {3}",a,b,c,res))
        return res

    
    def match(self, c1,c2):
        rM = c1[0] / c2[0]
        gM = c1[1] / c2[1]
        bM = c1[2] / c2[2]
        avg = (rM + gM + bM) / 3.0
        return avg
        
    def update(self):
        self.panel.setBackground(self.curColor)
        #print(self.curColor)
        curR = self.lerp(self.color2[0], self.curColor[0],self.speed)
        curG = self.lerp(self.color2[1], self.curColor[1],self.speed)
        curB = self.lerp(self.color2[2], self.curColor[2],self.speed)
        self.curColor = (curR,curG,curB)
        if (self.match(self.curColor, self.color2) > 0.99):
            self.color2 = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
