import pyxel
pyxel.init(128, 128, title="NDC 2024")
pyxel.load("theme2.pyxres")

px = 64
py = 64

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
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    
    depv()

def draw():
    pyxel.blt(px,py,0,0,0,16,16,0)

pyxel.run(update,draw)
