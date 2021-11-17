# File name: player.py

# We'll need a BooleanProperty for the bankrupt property.
from kivy.properties import (StringProperty, NumericProperty, 
                             ObjectProperty, BooleanProperty)
from kivy.event import EventDispatcher

class Player(EventDispatcher):
    name = StringProperty('')
    initial_money = NumericProperty(0)  
    money = NumericProperty(0)               
    money_before_race = NumericProperty(0)  
    money_won = NumericProperty(0)  
    bet = NumericProperty(1) 
    chosen_slug = ObjectProperty(None, allownone=True)

    # Here's the bankrupt property. By default it's set to False.
    bankrupt = BooleanProperty(False)

    def update(self, winning_slug):
        self.money_before_race = self.money 
        self.money_won = (int(self.bet * (winning_slug.odds - 1)) 
                          if self.chosen_slug == winning_slug 
                          else -self.bet) 
        self.money += self.money_won

        # If the player loses all money, the bankrupt 
        # property is set to True.
        if self.money == 0:
            self.bankrupt = True

    def reset(self):
        self.chosen_slug = None     
        self.bet = 1