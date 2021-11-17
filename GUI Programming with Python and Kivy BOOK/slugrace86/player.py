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

    # the slug the player bets on
    chosen_slug = ObjectProperty(None)