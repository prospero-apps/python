# File name: bets.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation

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

    def on_leave(self):
        self.clear_bets()
        self.main_layer.disabled = False

        # Let's cancel the animation here.
        self.race_label_animation.cancel(self.race_label)

    # Here's the method where we create and start the race label animation.
    def animate_race_label(self):
        # The animation should consist of two simple animations joined sequentially.
        self.race_label_animation = (Animation(color=[.2, .1, 0, 1], d=1) + 
                                     Animation(color=[.5, .1, 0, 1], d=1))

        # The animation should be repeated.                             
        self.race_label_animation.repeat = True

        # Let's start the animation.
        self.race_label_animation.start(self.race_label)
