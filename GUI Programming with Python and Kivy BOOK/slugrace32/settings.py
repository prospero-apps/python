# File name: settings.py

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SettingsApp(App):
    def build(self):
        return BoxLayout()

if __name__ == '__main__':
    SettingsApp().run()
