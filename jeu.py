import pyxel
pyxel.init(128, 128, title="NDC 2024")

def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
        
def draw():
    pyxel.rect(0,0,3,127,9)

pyxel.run(update,draw)
