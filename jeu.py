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
        if clef[0]-16<px<clef[0]+8 and clef[1]-16<py<clef[0]+16:
            clefs.remove(clef)

def depv():
    global x, y
    if pyxel.btn(pyxel.KEY_RIGHT) and pyxel.tilemap(0).pget(x//8+1,(y+4)//8) not in tuiles_inter:
        x += 1
    if pyxel.btn(pyxel.KEY_LEFT) and pyxel.tilemap(0).pget(x//8,(y+4)//8) not in tuiles_inter:
        x -= 1
    if pyxel.btn(pyxel.KEY_DOWN) and pyxel.tilemap(0).pget((x+4)//8,y//8+1) not in tuiles_inter:
        y += 1
    if pyxel.btn(pyxel.KEY_UP) and pyxel.tilemap(0).pget((x+4)//8,(y-1)//8) not in tuiles_inter:
        y -= 1
        
def update():
    depv()
    colli_joueur_clef()

def draw():
    pyxel.cls(0)
    pyxel.blt(px,py,0,32,0,16,16,0)
    for clef in clefs:
        pyxel.blt(clef[0],clef[1],0,0,16,8,16,0)

pyxel.run(update,draw)
