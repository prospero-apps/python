# File name: test.py

from kivy.app import App
from kivy.uix.slider import Slider

class TestApp(App):
    def build(self):
        return Slider()

if __name__ == '__main__':
    TestApp().run()