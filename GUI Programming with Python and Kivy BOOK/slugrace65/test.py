# File name: test.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '1')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class TestLayout(FloatLayout):
    label1 = ObjectProperty()
    label2 = ObjectProperty()
    button1 = ObjectProperty()
    button2 = ObjectProperty()
    slider = ObjectProperty()

    # Here are the three new properties.
    button3 = ObjectProperty()
    button4 = ObjectProperty()
    button5 = ObjectProperty()

    def on_touch_down(self, touch):
        self.label1.text = str(int(touch.x))
        self.label2.text = str(int(touch.y))
        self.button1.font_size += 1
        self.button2.text += '+'
        self.slider.value += 1

    # This method is called when you move the mouse with the left mouse 
    # button down.
    def on_touch_move(self, touch):
        # The text on button 3 should display the position of the mouse.
        self.button3.text = f'x = {int(touch.x)}\ny = {int(touch.y)}'

        # Button 4 should follow the mouse.
        self.button4.center = [touch.x, touch.y]

    # This method is called when you release the mouse button.
    def on_touch_up(self, touch):
        # The width of button 5 should be halved.
        self.button5.size_hint_x /= 2

class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()
