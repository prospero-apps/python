# File name: test.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class TestScreen(GridLayout):
    pass

class TestApp(App):
    def build(self):
        return TestScreen()

if __name__ == '__main__':
    TestApp().run()
