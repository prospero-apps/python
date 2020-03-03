# File name: main.py

import kivy
from kivy.app import App

# This is what you need to import in order to use a slider.
from kivy.uix.slider import Slider

class HelloWorldApp(App):
    def build(self):
        # Now we want a slider to be returned.
        return Slider()

if __name__ == '__main__':
    HelloWorldApp().run()