import pyxel
import math
pyxel.init(128, 128, title="NDC 2024")
pyxel.load("theme2.pyxres")

#joueur
px = 64
py = 64

#cam
cpx = px-60

cpy = py-60

#clefs (3)
clefs = [(0,10),(64,58),(100,12)]
#coffre


def colli_joueur_clef():
    global clefs
    for clef in clefs:
        if clef[0]-16<px<clef[0]+8 and clef[1]-16<py<clef[0]+16:
            clefs.remove(clef)

def depv():
    global px, py
    if pyxel.btn(pyxel.KEY_RIGHT):
        px += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        px -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        py += 1
    if pyxel.btn(pyxel.KEY_UP):
        py -= 1
        
def update():
    depv()
    colli_joueur_clef()

def draw():
    pyxel.cls(3)
    pyxel.blt(px,py,0,32,0,16,16,0)
    pyxel.bltm(0,0,0,0,0,128,128)
    pyxel.camera(cpx,cpy)
    for clef in clefs:
        pyxel.blt(clef[0],clef[1],0,0,16,8,16,0)

pyxel.run(update,draw)
