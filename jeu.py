import pyxel
pyxel.init(128, 128, title="NDC 2024")

def update():
    if pyxel.btn(pyxel.KEY_SPACE):
        print("test")
        print("j'en pasaoifdhuzgfyzieufgzefpas ai ma   rre erighergkuygeuyerhguydehgueguerhiuergh")
        print("ofuhefiuh")

def draw():
    pyxel.rect(0,0,3,3,9)


pyxel.run(update,draw)
