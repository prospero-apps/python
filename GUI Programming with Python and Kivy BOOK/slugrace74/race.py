# File name: race.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file('bets.kv')
Builder.load_file('results.kv')

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
    body_image = StringProperty('speedsterBody')
    eye_image = StringProperty('speedsterEye')
    y_position = NumericProperty(0)

class RaceScreen(Screen):
    pass