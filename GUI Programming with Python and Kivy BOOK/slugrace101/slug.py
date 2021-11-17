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

    # This method will just reset the slug to his start position.
    def reset(self):
        self.pos_hint = {'x': self.start_position}
