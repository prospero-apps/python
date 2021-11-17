# File name: test.py

from kivy.app import App

# We must import the AnchorLayout class.
from kivy.uix.anchorlayout import AnchorLayout

class TestApp(App):
    def build(self):
        # We're going to use the AnchorLayout now.
        return AnchorLayout()

if __name__ == '__main__':
    TestApp().run()
