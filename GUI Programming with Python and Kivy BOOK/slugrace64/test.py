# File name: test.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '1')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class TestLayout(FloatLayout):
    pass

class CustomLayout(BoxLayout):
    def move_slider(self):
        if self.ids._slider.value <= self.ids._slider.max - 5:
            self.ids._slider.value += 5

class CustomButton(Button):
    def set_text(self):
        self.parent.ids._label2.text = 'CHANGED' 

class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()
