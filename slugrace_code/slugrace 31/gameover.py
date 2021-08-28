# File name: gameover.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class GameoverScreen(BoxLayout):
    pass

class GameoverApp(App):
    def build(self):
        return GameoverScreen()

if __name__ == '__main__':
    GameoverApp().run()