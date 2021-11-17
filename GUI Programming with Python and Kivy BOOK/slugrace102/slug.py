# File name: slug.py

from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rotate_eyes(30, uniform(.3, 1.5))

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
        move_base = randint(1, 10)
        if move_base < self.speeds[0]:
            running_time = uniform(8, 10)  # slow
        elif move_base <= self.speeds[1]:
            running_time = uniform(6, 8)  # medium
        else:
            running_time = uniform(4, 6)  # fast

        self.run_animation = Animation(pos_hint={'x': self.finish_position}, 
                                       d=running_time)
        self.run_animation.start(self)

    def reset(self):
        self.pos_hint = {'x': self.start_position}

    def rotate_eyes(self, max_angle, duration):
        self.eye_animation = (Animation(rot_angle=max_angle, d=duration) + 
                              Animation(rot_angle=0, d=duration))
        self.eye_animation.repeat = True
        self.eye_animation.start(self)
