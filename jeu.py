import pyxel
import math
import random
pyxel.init(128, 128, title="NDC 2024")
pyxel.load("theme2.pyxres")

#joueur
px = 32
py = 32
nb_clefs = 0
#cam
cpx = px-60
cpy = py-60

capx = 0
capy = 0
#clefs (3)

#coffre

tuiles_inter = [(4,2),(2,2),(2,3),(3,2),(3,3)]

def hide():
    global px, py
    for i in range(px//8-24, px//8+24):
        for j in range(py//8-24, py//8+24):
            if math.sqrt((px-i*8)**2+(py-j*8)**2)>40:
                pyxel.rect(i*8,j*8,8,8,0)

def colli_joueur_clef():
    global nb_clefs
    if pyxel.tilemap(0).pget((px+8)//8,(py+8)//8) in [(0,2),(0,3)]:
        pyxel.tilemap(0).pset((px+8)//8,(py+8)//8,(0,0))
        nb_clefs+=1
        if pyxel.tilemap(0).pget((px+8)//8,(py+8)//8+1) in [(0,2),(0,3)]:
            pyxel.tilemap(0).pset((px+8)//8,(py+8)//8+1,(0,0))
        else:
            pyxel.tilemap(0).pset((px+8)//8,(py+8)//8-1,(0,0))

def spawn_coffre():
    if nb_clefs == 3:
        pyxel.tilemap(0).pset(16//8,16//8,(2,0))

def depv():
    global px, py
    if pyxel.btn(pyxel.KEY_RIGHT) and pyxel.tilemap(0).pget(px//8+2,(py)//8) not in tuiles_inter :
        px += 2
        
    if pyxel.btn(pyxel.KEY_LEFT) and pyxel.tilemap(0).pget((px-2)//8,(py)//8) not in tuiles_inter:
        px -= 2
    if pyxel.btn(pyxel.KEY_DOWN) and pyxel.tilemap(0).pget(px//8,(py)//8+2) not in tuiles_inter:
        py += 2
    if pyxel.btn(pyxel.KEY_UP) and pyxel.tilemap(0).pget(px//8+1,(py-2)//8) not in tuiles_inter:
        py -= 2

def cam():
    global cpx, cpy, px, py
    cpx = px-60
    cpy = py-60
    if py<60:
        cpy = 0
    if py>322:
        cpy = 256
    if px<60:
        cpx = 0
    if px>322:
        cpx = 256

def carte():
    global px, py, capx, capy
    
    capx = px-50
    capy = py-50
    
    if px<=60:
        capx = 10
    
    if py<=60:
        capy = 10
    
    if px>=(384-62):
        capx = 384-118
    
    if py>=(384-62):
        capy = 384-118
        
        
    

def update():
    depv()
    colli_joueur_clef()
    cam()
    spawn_coffre()
    carte()
    
def draw():
    pyxel.cls(3)
    pyxel.bltm(0,0,0,0,0,384,384)
    hide()
    pyxel.blt(px,py,0,32,0,16,16,0)
    pyxel.blt(capx,capy,0,0,32,16,16,0)
    pyxel.blt((capx+1+px/32),(capy+1+py/32),0,16,32,1,1,0)

    pyxel.camera(cpx,cpy)

pyxel.run(update,draw)
