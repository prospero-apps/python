# File name: player.py

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
    bankrupt = BooleanProperty(False)

    def update(self, winning_slug):
        self.money_before_race = self.money 
        self.money_won = (int(self.bet * (winning_slug.odds - 1)) 
                          if self.chosen_slug == winning_slug 
                          else -self.bet) 
        self.money += self.money_won

        if self.money == 0:
            self.bankrupt = True

    # Now there's the gameover parameter, 
    # which will be set to True only
    # before a new game begins.
    def reset(self, gameover=False):
        self.chosen_slug = None     
        self.bet = 1

        # This code is only executed when we 
        # want to play again after the game 
        # is over, not after each race.
        if gameover:
            self.bankrupt = False
