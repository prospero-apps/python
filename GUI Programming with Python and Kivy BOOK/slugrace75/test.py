# File name: test.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '1')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from random import choice

class CustomButton(Button):    
    vowels = StringProperty('a') 

    def on_vowels(self, instance, value):
        if len(value) > 8:
            instance.vowels = value[-3:]
       
    def on_press(self):
        self.vowels += choice('aeiou')

class TestLayout(FloatLayout):  
    pass
    
class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()
