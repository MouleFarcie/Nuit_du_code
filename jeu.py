import pyxel
pyxel.init(128, 128, title="NDC 2024")
pyxel.load("theme2.pyxres")

#joueur
px = 64
py = 64

#clefs (3)
clefs = [(0,10),(64,58),(100,12)]
#coffre




def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
        
def draw():
    pyxel.blt(px,py,0,0,0,16,16,0)
    for clef in clefs:
        pyxel.blt(clef[0],clef[1],0,0,16,8,16,0)

pyxel.run(update,draw)
