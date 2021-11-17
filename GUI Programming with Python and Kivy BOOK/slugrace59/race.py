# File name: race.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class RaceScreen(BoxLayout):
    pass

class RaceApp(App):
    def build(self):
        return RaceScreen()

if __name__ == '__main__':
    RaceApp().run()
