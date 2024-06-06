import pyxel
pyxel.init(128, 128, title="NDC 2024")
pyxel.load("theme2.pyxres")

#joueur
px = 64
py = 64

#clefs (3)
clefs = [(0,10),(64,58),(100,12)]
#coffre

def colli_joueur_clef():
    global clefs
    for clef in clefs:
        if clef[0]-16<px<clef[0]+8 and clef[1]+16<py<clef[0]+16:
            print("capture")


def depv():
    global px, py
    if pyxel.btn(pyxel.KEY_RIGHT) and px < 120:
        px += 1
    if pyxel.btn(pyxel.KEY_LEFT) and px > 0:
        px -= 1
    if pyxel.btn(pyxel.KEY_DOWN) and py < 120:
        py += 1
    if pyxel.btn(pyxel.KEY_UP) and py > 0:
        py -= 1

def update():
    depv()
    colli_joueur_clef()

def draw():
    pyxel.cls(0)
    pyxel.blt(px,py,0,0,0,16,16,0)
    for clef in clefs:
        pyxel.blt(clef[0],clef[1],0,0,16,8,16,0)

pyxel.run(update,draw)
