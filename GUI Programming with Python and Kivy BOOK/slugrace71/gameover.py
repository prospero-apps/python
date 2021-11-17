# File name: gameover.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# We need the Screen class.
from kivy.uix.screenmanager import Screen

Builder.load_file('widgets.kv')

# Now the root widget should inherit from 
# Screen instead of BoxLayout.
class GameoverScreen(Screen):
    pass

class GameoverApp(App):
    def build(self):
        return GameoverScreen()

if __name__ == '__main__':
    GameoverApp().run()
