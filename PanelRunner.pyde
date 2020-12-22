from Panel import Panel
from Square import Square
from SinWave import SinWave
import random
p = Panel()
squares = []
wave = SinWave(p)

def setup():
    frameRate(15)
    size(800,800)
    wave = SinWave(p)
    

def draw():
    background(0)
    #p.setBackground((155,50,50))
    wave.update()
    p.show()
    fill(255)
    text(int(frameRate), width - 50, height - 50)