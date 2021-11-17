# File name: test.py

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class TestApp(App):
    def build(self):
        return ToggleButton()

if __name__ == '__main__':
    TestApp().run()