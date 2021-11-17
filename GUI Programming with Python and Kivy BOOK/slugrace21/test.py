# File name: test.py

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class TestApp(App):
    def build(self):
        return RelativeLayout()

if __name__ == '__main__':
    TestApp().run()
