# File name: player.py

# We need some property classes.
from kivy.properties import StringProperty, NumericProperty

# We need this to use Kivy properties at all.
from kivy.event import EventDispatcher

# The class must inherit from EventDispatcher.
class Player(EventDispatcher):
    name = StringProperty('')
    initial_money = NumericProperty(0)  
    money = NumericProperty(0)               
    money_before_race = NumericProperty(0)  
    money_won = NumericProperty(0)  
    bet = NumericProperty(1) 
