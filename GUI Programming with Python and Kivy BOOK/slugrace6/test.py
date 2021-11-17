# File name: test.py

from kivy.app import App
from kivy.uix.switch import Switch 

class TestApp(App):
    def build(self):
        return Switch()

if __name__ == '__main__':
    TestApp().run()