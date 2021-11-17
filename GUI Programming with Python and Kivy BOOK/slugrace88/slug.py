# File name: slug.py

from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty, NumericProperty

class Slug(RelativeLayout):
    name = StringProperty('')
    body_image = StringProperty('')
    eye_image = StringProperty('')
    front_image = StringProperty('')
    y_position = NumericProperty(0)
    wins = NumericProperty(0)  
    win_percent = NumericProperty(0) 
    odds = NumericProperty(0)

    # We need the race_number parameter to calculate the win percent.
    def update(self, winning_slug, race_number): 
        # update odds
        if self == winning_slug:
            self.odds = round(max(1.01, min(self.odds * .96, 20)), 2)
        else:
            self.odds = round(max(1.01, min(self.odds * 1.03, 20)), 2)

        # update wins and win_percent
        # The number of wins should be incremented only for the winner.
        if self == winning_slug:
            self.wins += 1

        # The win percent should be calculated regardless of whether the slug has won.    
        self.win_percent = round(self.wins / race_number * 100, 2)

