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

# Besides Screen we have to import ScreenManager.
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file('widgets.kv')

# Load the Bets and Results kv files.
Builder.load_file('bets.kv')
Builder.load_file('results.kv')

# Here's the screen manager class.
class RaceScreenManager(ScreenManager):
    pass

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
