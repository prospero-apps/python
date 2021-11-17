# File name: player.py

from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.event import EventDispatcher

class Player(EventDispatcher):
    name = StringProperty('')
    initial_money = NumericProperty(0)  
    money = NumericProperty(0)               
    money_before_race = NumericProperty(0)  
    money_won = NumericProperty(0)  
    bet = NumericProperty(1) 
    chosen_slug = ObjectProperty(None, allownone=True)

    def update(self, winning_slug):
        self.money_before_race = self.money 
        self.money_won = (int(self.bet * (winning_slug.odds - 1)) 
                          if self.chosen_slug == winning_slug 
                          else -self.bet) 
        self.money += self.money_won
