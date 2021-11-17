# File name: test.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '1')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# We don't need the NumericProperty anymore, 
# but we need the ListProperty.
from kivy.properties import ListProperty

from kivy.uix.button import Button

class CustomButton(Button): 
    # Here's the property.
    enemies = ListProperty([])

    # And here's the method that will be called each time
    # the enemies property changes, for example when new
    # elements are appended like in this program.
    def on_enemies(self, instance, value):
        if len(value) > 5:
            self.text = 'Beware. There are more \nand more enemies!'

class TestLayout(BoxLayout): 
    pass

class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()
