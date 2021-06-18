# We need the ShowBase class, so let's import it.
from direct.showbase.ShowBase import ShowBase

# Here comes the application class. It inherits from ShowBase. 
class Slugrace3D(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

# And this is where we actually create and run the app.
app = Slugrace3D()
app.run()
