import pyxel
import math
import random
pyxel.init(128, 128, title="NDC 2024")
pyxel.load("theme2.pyxres")

#joueur
px = 70
py = 70
nb_clefs = 0
#cam
cpx = px-60
cpy = py-60

#clefs (3)
clefs = []
#coffre

def hide():
    global px, py
    for i in range(px//8, px//8+17):
        for j in range(16):
            if math.sqrt((px+60-i*8)**2+(py+60-j*8)**2)>40:
                pyxel.rect(i*8,j*8,8,8,2)

def colli_joueur_clef():
    global clefs, nb_clefs
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
    if pyxel.btn(pyxel.KEY_RIGHT) :
        px += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        px -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        py += 1
    if pyxel.btn(pyxel.KEY_UP):
        py -= 1

def cam():
    global cpx, cpy, px, py
    cpx = px-60
    cpy = py-60
    if py<60:
        cpy = 0
    if py>186:
        cpy = 128
    if px<60:
        cpx = 0
    if px>186:
        cpx = 128

def update():
    depv()
    colli_joueur_clef()
    hide()
    cam()
    spawn_coffre()

def draw():
    pyxel.cls(3)
    pyxel.bltm(0,0,0,0,0,256,256)
    pyxel.blt(px,py,0,32,0,16,16,0)
    



    for clef in clefs:
        pyxel.blt(clef[0],clef[1],0,0,16,8,16,0)
    pyxel.camera(cpx,cpy)

pyxel.run(update,draw)
