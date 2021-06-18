from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class Slugrace3D(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        props = WindowProperties()
        props.setTitle('Test Game')
        props.setSize(1200, 675)

        # Hide the mouse cursor when hovering over the app window.
        props.setCursorHidden(True)      

        base.win.requestProperties(props)

app = Slugrace3D()
app.run()

