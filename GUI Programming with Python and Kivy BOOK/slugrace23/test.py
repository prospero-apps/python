# File name: test.py

from kivy.app import App

# We must import the BoxLayout class.
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):
    def build(self):
        # We're going to use the BoxLayout now.
        return BoxLayout()

if __name__ == '__main__':
    TestApp().run()