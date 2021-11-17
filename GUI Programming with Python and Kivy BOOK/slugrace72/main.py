# File name: main.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

# We need the Builder class to load kv files.
from kivy.lang import Builder

# We must load the kv files of the three screens.
Builder.load_file('settings.kv')
Builder.load_file('race.kv')
Builder.load_file('gameover.kv')

class SlugraceScreenManager(ScreenManager):
    pass

class SlugraceApp(App):
    def build(self):
        return SlugraceScreenManager()

if __name__ == '__main__':
    SlugraceApp().run()
