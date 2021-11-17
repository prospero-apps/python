# File name: test.py

from kivy.app import App

# We'll need the Widget class 
# to inherit from.
from kivy.uix.widget import Widget

# Here is the inheritance. 
class MyCustomWidget(Widget):
    # We're going to implement it 
    # in the kv file.
    pass

class TestApp(App):
    def build(self):
        # Now we want our custom 
        # widget to be returned.
        return MyCustomWidget()

if __name__ == '__main__':
    TestApp().run()