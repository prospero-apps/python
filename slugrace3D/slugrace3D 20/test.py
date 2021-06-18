# File name: test.py

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from panda3d.core import load_prc_file

# We need the Actor class to load actors.
from direct.actor.Actor import Actor

import simplepbr

load_prc_file('myConfig.prc')

class Slugrace3D(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        simplepbr.init()

        # Let's load and position the terrain.
        self.terrain = loader.loadModel("models/terrain/terrain.gltf")
        self.terrain.setPos(0, 0, -1)
        self.terrain.reparentTo(render)           

        # Let's import, position, scale and rotate the actor.
        self.slug = Actor("actors/slug/slug.gltf")
        self.slug.setPos(0, 0, -1)
        self.slug.setScale(10, 10, 10)
        self.slug.setH(90)
        self.slug.reparentTo(render) 

        # play animation
        self.slug.loop('idle')

app = Slugrace3D()
app.run()
