from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from panda3d.core import load_prc_file

# We need to import simplepbr.
import simplepbr

load_prc_file('myConfig.prc')

class Slugrace3D(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # We must call simplepbr's init method here.
        simplepbr.init()

        self.building = loader.loadModel("models/building/building.gltf")
        self.building.setPos(0, 50, 0)
        self.building.reparentTo(render)   
        
app = Slugrace3D()
app.run()

