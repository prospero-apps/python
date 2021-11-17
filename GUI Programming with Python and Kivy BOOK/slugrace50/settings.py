# File name: settings.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SettingsScreen(BoxLayout):
    pass

class SettingsApp(App):
    def build(self):
        return SettingsScreen()

if __name__ == '__main__':
    SettingsApp().run()
