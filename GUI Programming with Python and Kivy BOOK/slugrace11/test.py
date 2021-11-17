# File name: test.py

from kivy.app import App
from kivy.uix.textinput import TextInput

class TestApp(App):
    def build(self):
        return TextInput()

if __name__ == '__main__':
    TestApp().run()