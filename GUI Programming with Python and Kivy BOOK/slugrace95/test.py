# File name: test.py

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

class TestLayout(FloatLayout):  
    def handle_move(self):
        Clock.schedule_interval(self.move, .1)

    def move(self, dt):
        if self.button.right < self.right:
            self.button.x += 20
        else:
            self.button.x = 20
        
class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()
