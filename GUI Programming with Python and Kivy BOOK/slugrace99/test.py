# File name: test.py

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

class TestLayout(FloatLayout): 
    def start_animations(self):        
        # save the button's initial x position for future use
        start_x = self.button.x

        # save the button's background color for future use
        button_color = self.button.background_color

        # Let's create an animation consisting of two animations joined 
        # sequentially to animate the x position of the button. It will 
        # move to the right in three seconds and then back to the left 
        # in half a second.
        pos_anim = Animation(x=400, d=3) + Animation(x=start_x, d=.5)

        # Let's create another animation consisting of two animations 
        # joined sequentially to animate the background color of the button. 
        # It will change to red in 0.2 seconds and then back to its original 
        # color in 0.1 seconds. This will make the button pulsate.
        color_anim = (Animation(background_color=[1, 0, 0, 1], d=.2) 
                     + Animation(background_color=button_color, d=.1))

        # set the animations to repeat
        pos_anim.repeat = True
        color_anim.repeat = True

        # Let's make the two combined animations run in parallel.
        anim = pos_anim & color_anim

        # start the combined animation
        anim.start(self.button)
        
class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()