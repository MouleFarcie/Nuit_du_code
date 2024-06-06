import pyxel
import math
import random
pyxel.init(128, 128, title="NDC 2024")
pyxel.load("theme2.pyxres")

menu = 0
sens = 1
time = 0

cocx = 24*8
cocy = 24*8

ang1 = 0
ang2 = 0
dire1 = 1
dire2 = 1
boux = 0
bouy = 0


#joueur
px = 32
py = 32
nb_clefs = 0
vie = 3

#blobs
blob = [192,192,"left"]

#cam
cpx = px-60
cpy = py-60

capx = 0
capy = 0

ccx = 1
ccy = 1

tuiles_inter = [(4,2),(2,2),(2,3),(3,2),(3,3)]

def hide():
    global px, py
    for i in range(px//8-24, px//8+24):
        for j in range(py//8-24, py//8+24):
            if math.sqrt((px-i*8)**2+(py-j*8)**2)>40:
                pyxel.rect(i*8,j*8,8,8,0)


def blob_dep():
    global blob
    if pyxel.frame_count-time>150:
        if blob[0]<px:
            blob[0]+=1
            blob[2] = "right"
        elif blob[0]>px:
            blob[0]-=1
            blob[2] = "left"
        if blob[1]<py:
            blob[1]+=1
        elif blob[1]>py:
            blob[1]-=1

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

    global t
    if nb_clefs == 3:
        t = 1
        pyxel.tilemap(0).pset(24,24,(2,0))
        pyxel.tilemap(0).pset(24+1,24,(3,0))
        pyxel.tilemap(0).pset(24,24+1,(2,1))
        pyxel.tilemap(0).pset(24+1,24+1,(3,1))

def col_coffre():
    global menu
    if nb_clefs == 3:
        if pyxel.tilemap(0).pget((px+8)//8,(py+8)//8) in [(2,0),(3,0),(3,1),(2,1)]:
            pyxel.tilemap(0).pset((px+8)//8,(py+8)//8,(0,0))

            if pyxel.tilemap(0).pget((px+8)//8,(py+8)//8+1) in [(2,0),(3,0),(3,1),(2,1)]:
                menu = 3

def depv():
    global px, py
    if pyxel.btn(pyxel.KEY_RIGHT) and pyxel.tilemap(0).pget(px//8+2,(py+7)//8) not in tuiles_inter :
        px += 2
        
    if pyxel.btn(pyxel.KEY_LEFT) and pyxel.tilemap(0).pget((px-2)//8,(py+7)//8) not in tuiles_inter:
        px -= 2
    if pyxel.btn(pyxel.KEY_DOWN) and pyxel.tilemap(0).pget((px+7)//8,(py)//8+2) not in tuiles_inter:
        py += 2
    if pyxel.btn(pyxel.KEY_UP) and pyxel.tilemap(0).pget((px+7)//8,(py-2)//8) not in tuiles_inter:
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

def boussole():
    global ang1, ang2, dire1, dire2, boux, bouy
    
    ang1 = px - cocx
    
    ang2 = py - cocy
    
    if ang1 <0:
        dire1 = 1
        
    if ang1 >0:
        dire1 = 2
    
    
    if ang2 <0:
        dire2 = 1
        
    if ang2 >0:
        dire2 = 2
        
    if dire1 == 1 and dire2 == 1:
        boux = 48
        bouy = 24
        
    if dire1 == 1 and dire2 == 2:
        boux = 40
        bouy = 16
    
    if dire1 == 2 and dire2 == 2:
        boux = 40
        bouy = 24
    
    if dire1 == 2 and dire2 == 1:
        boux = 48
        bouy = 16
        
    if ang1 == 0 and ang2 > 0 :
        boux = 64
        bouy = 24
        
    if ang1 == 0 and ang2 < 0 :
        boux = 56
        bouy = 24
        
    if ang2 == 0 and ang1 > 0 :
        boux = 64
        bouy = 16
        
    if ang2 == 0 and ang1 < 0 :
        boux = 56
        bouy = 16

def menuu():
    global ccx, ccy, menu, sens, time
    
    if menu == 0:
        if ccx == 248:
            sens = -1
        if ccx == 1:
            sens = 1
        ccx += sens
        ccy += sens
            

    if pyxel.btn(pyxel.KEY_SPACE):
        menu = 1
        time = pyxel.frame_count
    
    if vie <= 0:
        menu = 2

def colli_joueur_blob():
    global vie, time, menu
    if blob[0]-16<px<blob[0]+12 and blob[1]-16<py<blob[1]+12 and pyxel.frame_count-time>150:
        vie-=1
        print("touché")
        time = pyxel.frame_count
        if vie == 0:
            menu = 2
def update():
    menuu()
    if menu==1:
        depv()
        colli_joueur_clef()
        cam()
        spawn_coffre()
        carte()
        boussole()
        #blob_dep()
        colli_joueur_blob()
        col_coffre()
        
def draw():
    pyxel.cls(3)
    if menu !=2 and menu!= 3:
        pyxel.bltm(0,0,0,0,0,384,384)

    if menu == 0:
        pyxel.camera(ccx,ccy)
        pyxel.text(ccx+30, ccy+100, "PRESS SPACE TO START", 5)
        pyxel.text(ccx+50, ccy+50, "Labymine", 5)
    if menu == 1:
        hide()
        if pyxel.frame_count%30<15:
            pyxel.blt(px,py,0,32,0,16,16,0)
        else:
            pyxel.blt(px,py,0,48,0,16,16,0)

        pyxel.blt(capx,capy,0,0,32,16,16,0)

        pyxel.blt((capx+1+px/28),(capy+1+py/28),0,16,32,1,1,0)

        pyxel.blt(capx,capy+20,0,boux,bouy,8,8,0)

        pyxel.text(capx+20,capy,"clefs :"+str(nb_clefs), 5)
        
        pyxel.text(capx+20,capy+10,"vie :"+str(vie),5)

        pyxel.camera(cpx,cpy)
        if blob[2] == "right":
            pyxel.blt(blob[0],blob[1],0,18,52,12,12,0)
        elif blob[2] == "left":
            pyxel.blt(blob[0],blob[1],0,2,52,12,12,0)

        
    if menu==2:
        pyxel.text(blob[0]-10, blob[1]-10, "GAME OVER", 0)
    
    if menu==3:
        pyxel.text(px-20, py-20, "CONGRATULATIONS", 0)

pyxel.run(update,draw)