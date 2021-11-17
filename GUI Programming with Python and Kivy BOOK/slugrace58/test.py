# File name: test.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '1')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

# We will need some classes.
from kivy.graphics import Line, Color, Translate, Scale, PushMatrix, PopMatrix
from kivy.uix.label import Label

class TestLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:  
            # Save the context.
            PushMatrix()

            # Set color to green.        
            Color(0, 1, 0, 1)  

            # Draw the first line.
            Line(points=(100, 100, 120, 200, 150, 120, 180, 150, 200, 100), 
                 width=5, close=True)

            # Scale the coordinate space.
            Scale(2, 2, 0, origin=(100, 100))

            # Translate the coordinate space.  
            Translate(200, 0)

            # Draw the second line.
            Line(points=(100, 100, 120, 200, 150, 120, 180, 150, 200, 100), 
                 width=5, close=True)

            # Restore the saved context.
            PopMatrix()

        # Add the label.
        self.add_widget(Label(text='Done', font_size=40, pos=(100, 200), 
                              size_hint=(None, None), size=(100, 50)))

class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()
