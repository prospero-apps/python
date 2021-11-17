# File name: test.py

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

# We'll need the Button class and the randint function.
from kivy.uix.button import Button
from random import randint

class CustomButton(Button):
    # When the button is pressed, the animation should be created and started.
    # We pass a random integer number between 1 and 5 to the animate method.
    def on_press(self):
        self.animate(randint(1, 5))

    # The animate method takes the time argument which it uses to set
    # the duration of the animation.
    def animate(self, time):  
        # We're going to animate two properties of the button: pos_hint 
        # and background_color.
        self.anim = Animation(pos_hint={'center_y': .8}, 
                              background_color=[0, 1, 0, 1], 
                              d=time) 

        # Here are the bindings to the custom methods.
        self.anim.bind(on_start=self.on_start)
        self.anim.bind(on_progress=self.on_progress)
        self.anim.bind(on_complete=self.on_complete)

        # Here we start the animation on the button itself.
        self.anim.start(self)
    
    # When the animation starts, the text color on the button changes to white.
    def on_start(self, instance, value):
        self.color = [1, 1, 1, 1] # white        

    # During the first half of the animation the font size of the button text
    # decreases, during the second half it increases again.
    def on_progress(self, instance, value, progression): 
        if progression < .5:
            self.font_size -= .4
        else:
            self.font_size += .4

    # When the animation finishes, the button becomes fully transparent.
    def on_complete(self, instance, value):
        self.opacity = 0        

class TestLayout(FloatLayout): 
    pass
            
class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()