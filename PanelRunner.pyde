from Panel import Panel
from Square import Square
from Square import BouncingSquares
import time
import random
from Disperse import Disperse
from Scene import Scene
from SceneManager import SceneManager
#from ImgSizer import ImgSizer
from SinWave import SinWave
from ColorLerp import ColorLerp

import random
p = Panel()
p = Panel()
sceneManager = SceneManager()
#sceneManager.addScene(Scene(ImgSizer("LIKEWILDEBLACK.png", p),  5))
#sceneManager.addScene(Scene(Disperse(10,p), 14, True))
#sceneManager.addScene(Scene(ImgSizer("Mario.png", p), 8))
#sceneManager.addScene(Scene(Disperse(10,p), 14, True))
# sceneManager.addScene(Scene(SinWave(p), 20))
# sceneManager.addScene(Scene(BouncingSquares(1,1,20,p), 10))
# sceneManager.addScene(Scene(BouncingSquares(4,4,10,p), 10))
# sceneManager.addScene(Scene(BouncingSquares(3,3,20,p), 10))
sceneManager.addScene(Scene(ColorLerp(0.1,p), 20))


def setup():
    frameRate(15)
    size(800,800)
    

def draw():
    background(0)
    #p.setBackground((155,50,50))
    sceneManager.update()
    p.show()
    fill(255)
    text(int(frameRate), width - 50, height - 50)
