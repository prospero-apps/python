# File name: slug.py

from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import (StringProperty, 
                            NumericProperty, 
                            ListProperty, 
                            BooleanProperty)
from kivy.animation import Animation
from random import randint, uniform

class Slug(RelativeLayout):
    name = StringProperty('')
    body_image = StringProperty('')
    eye_image = StringProperty('')
    front_image = StringProperty('')
    y_position = NumericProperty(0)
    wins = NumericProperty(0)  
    win_percent = NumericProperty(0) 
    odds = NumericProperty(0)
    start_position = NumericProperty(.09)
    finish_position = NumericProperty(.83)
    speeds = ListProperty([])
    rot_angle = NumericProperty(0)
    finished = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Let's change the duration range from 
        # (0.3, 1.5) to (0.6 to 1.6).
        self.rotate_eyes(30, uniform(.6, 1.6))

    def update(self, winning_slug, race_number): 
        # odds
        if self == winning_slug:
            self.odds = round(max(1.01, min(self.odds * .96, 20)), 2)
        else:
            self.odds = round(max(1.01, min(self.odds * 1.03, 20)), 2)

        # wins and win_percent
        if self == winning_slug:
            self.wins += 1 
        self.win_percent = round(self.wins / race_number * 100, 2)

    def run(self):
        self.finished = False

        move_base = randint(1, 10)
        if move_base < self.speeds[0]:
            running_time = uniform(8, 10)  # slow
        elif move_base <= self.speeds[1]:
            running_time = uniform(6, 8)  # medium
        else:
            running_time = uniform(4, 6)  # fast

        # Cancel the eye animation.
        self.eye_animation.cancel(self)

        # Call the rotate_eyes method again so that 
        # a new eye animation is created with the same 
        # maximum angle, but with duration depending 
        # on the running time. 
        self.rotate_eyes(30, running_time/6)

        self.run_animation = Animation(pos_hint={'x': self.finish_position}, 
                                       d=running_time)
        return self.run_animation

    def reset(self):
        self.pos_hint = {'x': self.start_position}

    def rotate_eyes(self, max_angle, duration):
        self.eye_animation = (Animation(rot_angle=max_angle, d=duration) + 
                              Animation(rot_angle=0, d=duration))
        self.eye_animation.repeat = True
        self.eye_animation.start(self)
