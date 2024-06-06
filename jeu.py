import pyxel
pyxel.init(128, 128, title="NDC 2024")
pyxel.load("theme2.pyxres")

px = 64
py = 64

def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
        
def draw():
    pyxel.blt(px,py,0,0,0,16,16,0)

pyxel.run(update,draw)
