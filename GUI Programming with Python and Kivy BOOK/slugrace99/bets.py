# File name: bets.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen

class Bet(BoxLayout):
    player_name = StringProperty('')
    bet_amount = NumericProperty(0)
    max_bet_amount = NumericProperty(0)
    player_group = StringProperty('')
    selected_slug = NumericProperty(0)    

    def update_player_bet(self, player):
        player.bet = self.bet_amount

class BetsScreen(Screen):
    all_slugs_selected = BooleanProperty(False)

    def select_slug(self, player, slug_index):
        if slug_index >= 0:
            player.chosen_slug = self.game.slugs[slug_index]
            players_with_slugs = [player for player in self.game.players 
                                if player.chosen_slug]
            self.all_slugs_selected = len(players_with_slugs) == len(self.game.players)

    def clear_bets(self):
        self.all_slugs_selected = False
        
        for bet in self.bets:
            for slug_button in bet.slug_buttons:
                if slug_button.active:
                    slug_button.active = False
