# File name: settings.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SettingsScreen(BoxLayout):
    pass

class SettingsApp(App):
    def build(self):
        return SettingsScreen()

if __name__ == '__main__':
    SettingsApp().run()
