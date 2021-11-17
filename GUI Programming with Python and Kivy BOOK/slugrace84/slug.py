# File name: slug.py

from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty, NumericProperty

class Slug(RelativeLayout):
    body_image = StringProperty('')
    eye_image = StringProperty('')
    y_position = NumericProperty(0)

    # how many times the slug has won so far
    wins = NumericProperty(0)    

    # percent of races won by this particular slug
    win_percent = NumericProperty(0)  

    # the current odds for the slug - they will change after each race  
    odds = NumericProperty(0)

