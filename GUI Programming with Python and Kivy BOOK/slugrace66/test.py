# File name: test.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '1')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

# Don't forget to import the StringProperty as well.
from kivy.properties import NumericProperty, StringProperty

from kivy.uix.button import Button

# We'll need the Label class to inherit from.
from kivy.uix.label import Label

# Here's the CustomLabel class.
class CustomLabel(Label):
    # We need a StringProperty with the initial value of '*'.
    info = StringProperty('*')

    # When we click on the custom label, another star should
    # be appended at the end.
    def on_touch_down(self, touch):
        # This should only happen if we clicked inside the 
        # label's bounding box.
        if self.collide_point(touch.x, touch.y):
            self.info += '*'        

class CustomButton(Button):
    counter = NumericProperty(0)   

    def on_press(self):
        self.counter += 1

class TestLayout(FloatLayout):
    pass
    
class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()
