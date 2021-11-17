# File name: test.py

from kivy.app import App

# We'll be using the FloatLayout, so we have to import it.
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):
    def build(self):
        # Now we're going to return a FloatLayout. 
        # We'll define it in the kv file.
        return FloatLayout()

if __name__ == '__main__':
    TestApp().run()