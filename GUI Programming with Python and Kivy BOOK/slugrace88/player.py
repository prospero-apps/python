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
    chosen_slug = ObjectProperty(None)

    def update(self, winning_slug):
        # Let's save the current value of money so that we still have access to it
        # in the Results screen after it has changed.
        self.money_before_race = self.money  

        # The money that the player wins is:
        # a) the product of the bet amount and the slug's odds minus the bet amount,
        #    so self.bet * winning_slug.odds - self.bet, which can be more concisely
        #    written as self.bet * (winning_slug.odds - 1); it's rounded to an integer,
        # b) or the negative of the bet amount if the player loses.
        self.money_won = (int(self.bet * (winning_slug.odds - 1)) 
                          if self.chosen_slug == winning_slug 
                          else -self.bet)    

        # The money won by the player is added to their money. If the player loses, 
        # a negative number is added.
        self.money += self.money_won
