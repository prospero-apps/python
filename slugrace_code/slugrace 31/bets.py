# File name: bets.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class BetsScreen(BoxLayout):
    pass

class BetsApp(App):
    def build(self):
        return BetsScreen()

if __name__ == '__main__':
    BetsApp().run()