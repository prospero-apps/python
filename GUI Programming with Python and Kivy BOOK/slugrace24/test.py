# File name: test.py

from kivy.app import App

# We must import the StackLayout class.
from kivy.uix.stacklayout import StackLayout

class TestApp(App):
    def build(self):
        # We're going to use the StackLayout now.
        return StackLayout()

if __name__ == '__main__':
    TestApp().run()
