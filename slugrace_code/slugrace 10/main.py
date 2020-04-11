# File name: main.py

import kivy
from kivy.app import App
from kivy.uix.button import Button

# We'll be using the FloatLayout, so we have to import it.
from kivy.uix.floatlayout import FloatLayout

class HelloWorldApp(App):
    def build(self):
        # Now we're going to return a FloatLayout. We'll define it 
        # in the kv file.
        return FloatLayout()

if __name__ == '__main__':
    HelloWorldApp().run()