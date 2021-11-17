# File name: test.py

from kivy.app import App
from kivy.uix.checkbox import CheckBox

class TestApp(App):
    def build(self):
        return CheckBox()

if __name__ == '__main__':
    TestApp().run()