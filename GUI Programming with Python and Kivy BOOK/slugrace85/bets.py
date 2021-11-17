# File name: bets.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen

class Bet(BoxLayout):
    player_name = StringProperty('')
    bet_amount = NumericProperty(0)
    max_bet_amount = NumericProperty(0)
    player_group = StringProperty('')

    # Here's the method that will update the player's bet property
    # whenever the bet_amount property changes.
    def update_player_bet(self, player):
        player.bet = self.bet_amount

class BetsScreen(Screen):
    pass