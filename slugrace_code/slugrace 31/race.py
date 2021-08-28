# File name: race.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class RaceScreen(BoxLayout):
    pass

class RaceApp(App):
    def build(self):
        return RaceScreen()

if __name__ == '__main__':
    RaceApp().run()