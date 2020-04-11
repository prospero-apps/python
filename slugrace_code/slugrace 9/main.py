# File name: main.py

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyCustomButton(Button):
    pass

class MyCustomWidget(Widget):
    pass

class HelloWorldApp(App):
    def build(self):
        return MyCustomWidget()

if __name__ == '__main__':
    HelloWorldApp().run()