# File name: test.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '1')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.uix.button import Button

# We need to import the Slider class.
from kivy.uix.slider import Slider

class CustomButton(Button):
    counter = NumericProperty(0) 
       
    def on_press(self):
        self.counter += 1

        if self.counter > 2:
            self.unbind(on_press=paint_red)
            self.unbind(counter=make_bigger)
            self.unbind(counter=change_color)

class CustomSlider(Slider):
    # Override the on_value method.
    def on_value(self, instance, value):
        if value == 0:
            # The slider is now fully transparent, so unbind the
            # disappear function from the value property.
            self.unbind(value=disappear)

def make_bigger(instance, value):
    if value < 5:
        instance.font_size += 20

def change_color(instance, value):
    if instance.color == [1, 0, 0, 1]:
        instance.color = [0, 1, 0, 1]
    else:
        instance.color = [1, 0, 0, 1]  

def paint_red(instance):
    if instance.background_color == [1, 1, 1, 1]: # default
        instance.background_color = [1, 0, 0, 1]
    else:
        instance.background_color = [1, 1, 1, 1]

# Here's the function that we will bind to the value property.
def disappear(instance, value):
    # The value is always between min and max, so between 0 and 1
    # in this case. So is opacity, so they match easily.
    instance.opacity = value
 
class TestLayout(FloatLayout):  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.button1.bind(counter=make_bigger)
        self.button2.bind(counter=make_bigger)
        self.button2.bind(counter=change_color)
        self.button1.bind(on_press=paint_red)

        # Bind the disappear function to slider’s value property.
        self.slider.bind(value=disappear)

class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()
