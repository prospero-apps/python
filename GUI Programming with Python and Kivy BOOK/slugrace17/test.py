# File name: test.py

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.slider import Slider

class MyCustomButton(Button):
    pass

class MyCustomSlider(Slider):
    pass

class MyCustomWidget(Widget):
    pass

class TestApp(App):
    message = 'WELCOME'

    # Let's create another attribute.
    slider_value = 85
    
    def changeText(self, button):
        button.text = '***'

    # Let's define two other methods:
    def addTrack(self, slider, track_width):
        slider.value_track = True
        slider.value_track_width = track_width

    def removeTrack(self, slider):
        if slider.value_track:
            slider.value_track = False

    def build(self):
        return MyCustomWidget()

if __name__ == '__main__':
    TestApp().run()
