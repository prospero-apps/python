# File name: test.py

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

class TestLayout(FloatLayout): 

    # create and start two animations
    def start_animations(self):        
        self.anim1 = Animation(font_size=200, d=5)
        self.anim2 = Animation(color=[0, 1, 0, 1],
                              outline_width=20,
                              outline_color=[1, 0, 0, 1], 
                              d=5)
        self.anim1.start(self.label)
        self.anim2.start(self.label)

    # stop both animations
    def stop_all_animations(self):
        Animation.stop_all(self.label)

    # stop animating just the two color properties from the second animation
    def stop_color_animations(self):
        Animation.stop_all(self.label, 'color', 'outline_color')

    # stop animating the outline_width property from the second animation
    def stop_outline_animation(self):
        self.anim2.stop_property(self.label, 'outline_width')
        
class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()