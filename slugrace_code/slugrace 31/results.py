# File name: results.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class ResultsScreen(BoxLayout):
    pass

class ResultsApp(App):
    def build(self):
        return ResultsScreen()

if __name__ == '__main__':
    ResultsApp().run()