# File name: settings.py

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# the layout for the whole Settings screen
class SettingsScreen(BoxLayout):
    pass

class SettingsApp(App):
    def build(self):
        # We must return the SettingsScreen now.
        return SettingsScreen()

if __name__ == '__main__':
    SettingsApp().run()
