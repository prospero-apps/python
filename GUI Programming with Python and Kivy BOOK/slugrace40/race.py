# File name: race.py

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# root widget
class RaceScreen(BoxLayout):
    pass

class RaceApp(App):
    def build(self):
        return RaceScreen()

if __name__ == '__main__':
    RaceApp().run()
