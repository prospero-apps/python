# File name: race.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
Builder.load_file('widgets.kv')

class SlugStats(BoxLayout):
    name = StringProperty('')
    wins = NumericProperty(0)
    win_percent = NumericProperty(0)

class PlayerStats(BoxLayout):
    name = StringProperty('')
    money = NumericProperty(0)

class SlugInfo(BoxLayout):
    y_position = NumericProperty(0)
    name = StringProperty('')
    wins = NumericProperty(0)

class SlugImage(RelativeLayout):
    body_image = StringProperty('')
    eye_image = StringProperty('')
    y_position = NumericProperty(0)

class RaceScreen(Screen):
    pass

class RaceApp(App):
    def build(self):
        return RaceScreen()

if __name__ == '__main__':
    RaceApp().run()
