# File name: main.py

import kivy
from kivy.app import App
from kivy.uix.button import Label

class HelloWorldApp(App):
    def build(self):
        return Label()

if __name__ == '__main__':
    HelloWorldApp().run()