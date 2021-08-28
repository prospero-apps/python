# File name: test.py

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class TestLayout(FloatLayout):
    pass

class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()
