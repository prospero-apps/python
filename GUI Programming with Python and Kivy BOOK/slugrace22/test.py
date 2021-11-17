# File name: test.py

from kivy.app import App

# We must import the GridLayout class.
from kivy.uix.gridlayout import GridLayout

class TestApp(App):
    def build(self):
        # We're going to use the GridLayout now.
        return GridLayout()

if __name__ == '__main__':
    TestApp().run()

