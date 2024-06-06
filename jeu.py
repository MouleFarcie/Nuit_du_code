import pyxel
import math
import random
pyxel.init(128, 128, title="NDC 2024")
pyxel.load("theme2.pyxres")

menu = 0
sens = 1

cocx = 50
cocy = 70

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
blobs = []
temps_blob = 0
niveau = 1

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

def blobs_app():
    global blobs, temps_blob, niveau
    x = 0
    y = 0
    if pyxel.frame_count-temps_blob==30 and len(blobs)<5:
        while pyxel.tilemap(0).pget(x//8,y//8) in tuiles_inter:
            if niveau == 0 or niveau == 1:
                blobs.append([random.randint(0,384),random.randint(0,384),1,1,1,1,"right"])#x,y,vie,dégâts,vitesse ,niveau
                temps_blob = pyxel.frame_count
            elif niveau == 2:
                blobs.append([random.randint(0,384),random.randint(0,384),2,1,1,2,"right"])
                temps_blob = pyxel.frame_count
            elif niveau == 3:
                blobs.append([random.randint(0,384),random.randint(0,384),3,1,1,3,"right"])
                temps_blob = pyxel.frame_count
            else:
                print(niveau)
        if pyxel.frame_count-temps_blob>30:
            temps_blob = pyxel.frame_count

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
    
    print(ang1,ang2)
    
    if ang1 <0:
        print ("droite")
        dire1 = 1
        
    if ang1 >0:
        print ("gauche")
        dire1 = 2
    
    
    if ang2 <0:
        print ("bas")
        dire2 = 1
        
    if ang2 >0:
        print("haut")
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
    global ccx, ccy, menu, sens
    
    if menu == 0:
        if ccx == 248:
            sens = -1
        if ccx == 1:
            sens = 1
        ccx += sens
        ccy += sens
            

    if pyxel.btn(pyxel.KEY_SPACE):
        menu = 1
    

def update():
    depv()
    colli_joueur_clef()
    cam()
    spawn_coffre()
    carte()
    menuu()
    boussole()
def draw():
    pyxel.cls(3)
    pyxel.bltm(0,0,0,0,0,384,384)

    if menu == 0:
        pyxel.camera(ccx,ccy)
        pyxel.text(ccx+30, ccy+100, "PRESS SPACE TO START", 5)
    if menu == 1:
        hide()
        pyxel.blt(px,py,0,32,0,16,16,0)
        pyxel.blt(capx,capy,0,0,32,16,16,0)

        pyxel.blt((capx+1+px/28),(capy+1+py/28),0,16,32,1,1,0)

        pyxel.blt(capx,capy+20,0,boux,bouy,8,8,0)

        pyxel.camera(cpx,cpy)

        for blob in blobs:
            if blob[5] == 1 and blob[6] == "left":
                if pyxel.frame_count%30<10:
                    pyxel.blt(blob[0],blob[1],0,2,52,12,12,5)
                elif 10<=pyxel.frame_count%30<20:
                    pyxel.blt(blob[0],blob[1]+2,0,16,54,16,10,5)
                else:
                    pyxel.blt(blob[0],blob[1]+4,0,32,56,16,8,5)
            elif blob[5] == 1 and blob[6] == "right":
                if pyxel.frame_count%30<10:
                    pyxel.blt(blob[0],blob[1],0,50,52,12,12,5)
                elif 10<=pyxel.frame_count%30<20:
                    pyxel.blt(blob[0],blob[1]+2,0,64,54,16,10,5)
                else:
                    pyxel.blt(blob[0],blob[1]+4,0,80,56,16,8,5)
            elif blob[5] == 2 and blob[6] == "left":
                if pyxel.frame_count%30<10:
                    pyxel.blt(blob[0],blob[1],0,2,68,12,12,5)
                elif 10<=pyxel.frame_count%30<20:
                    pyxel.blt(blob[0],blob[1]+2,0,16,70,16,10,5)
                else:
                    pyxel.blt(blob[0],blob[1]+4,0,32,72,16,8,5)
            elif blob[5] == 2 and blob[6] == "right":
                if pyxel.frame_count%30<10:
                    pyxel.blt(blob[0],blob[1],0,50,68,12,12,5)
                elif 10<=pyxel.frame_count%30<20:
                    pyxel.blt(blob[0],blob[1]+2,0,64,70,16,10,5)
                else:
                    pyxel.blt(blob[0],blob[1]+4,0,80,72,16,8,5)
            elif blob[5] == 3 and blob[6] == "left":
                if pyxel.frame_count%30<10:
                    pyxel.blt(blob[0],blob[1],0,2,84,12,12,5)
                elif 10<=pyxel.frame_count%30<20:
                    pyxel.blt(blob[0],blob[1]+2,0,16,86,16,10,5)
                else:
                    pyxel.blt(blob[0],blob[1]+4,0,32,88,16,8,5)
            elif blob[5] == 3 and blob[6] == "right":
                if pyxel.frame_count%30<10:
                    pyxel.blt(blob[0],blob[1],0,50,84,12,12,5)
                elif 10<=pyxel.frame_count%30<20:
                    pyxel.blt(blob[0],blob[1]+2,0,64,86,16,10,5)
                else:
                    pyxel.blt(blob[0],blob[1]+4,0,80,88,16,8,5)

pyxel.run(update,draw)