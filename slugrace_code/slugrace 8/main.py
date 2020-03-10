# File name: main.py

import kivy
from kivy.app import App

# We're going to need the Button.
from kivy.uix.button import Button
from kivy.uix.widget import Widget

# Here is the inheritance. 
class MyCustomButton(Button):
    # We're going to implement it in the kv file.
    pass

class MyCustomWidget(Widget):
    # We're going to implement it in the kv file.
    pass

class HelloWorldApp(App):
    def build(self):
        return MyCustomWidget()

if __name__ == '__main__':
    HelloWorldApp().run()