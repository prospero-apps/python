from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from panda3d.core import load_prc_file
import simplepbr

load_prc_file('myConfig.prc')

class Slugrace3D(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        simplepbr.init()

        self.terrain = loader.loadModel("models/terrain/terrain.gltf")

        # Let's position the terrain.
        self.terrain.setPos(0, 0, -1)

        self.terrain.reparentTo(render)           

app = Slugrace3D()
app.run()
