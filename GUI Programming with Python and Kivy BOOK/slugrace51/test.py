# File name: test.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '1')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.widget import Widget

# We need the RoundedRectangle class.
from kivy.graphics import RoundedRectangle

class CustomWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()

    def update_canvas(self, *args):
        self.canvas.clear()    
        
        with self.canvas:
            RoundedRectangle(pos = (self.x + 20, self.y + 20), 
                             size = (self.width / 2, self.height / 3),
                             radius = [self.width / 10])

class TestApp(App):
    def build(self):
        return CustomWidget()

if __name__ == '__main__':
    TestApp().run()
