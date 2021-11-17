# File name: test.py

from kivy.app import App
from kivy.uix.widget import Widget

# We're going to need the Button and 
# the Slider.
from kivy.uix.button import Button
from kivy.uix.slider import Slider

# Here is the inheritance: we're defining 
# the MyCustomButton and MyCustomSlider
# classes that inherit from Button and 
# Slider respectively. We're leaving the
# implementation for the kv file.
class MyCustomButton(Button):
    pass

class MyCustomSlider(Slider):
    pass

class MyCustomWidget(Widget):
    pass

class TestApp(App):
    def build(self):
        return MyCustomWidget()

if __name__ == '__main__':
    TestApp().run()

