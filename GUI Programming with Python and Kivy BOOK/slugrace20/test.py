# File name: test.py

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):
    def build(self):
        return FloatLayout()

if __name__ == '__main__':
    TestApp().run()

