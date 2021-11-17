# File name: main.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from player import Player
from kivy.properties import (NumericProperty, BooleanProperty, 
                             StringProperty,  ObjectProperty)
from datetime import timedelta
from random import choice

Builder.load_file('settings.kv')
Builder.load_file('race.kv')
Builder.load_file('gameover.kv')
Builder.load_file('widgets.kv')
Builder.load_file('slug.kv')

class Game(ScreenManager):
    # the players
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()

    number_of_players = NumericProperty(2)
    players = [player1, player2]

    # ending conditions.
    end_by_money = BooleanProperty(True)
    end_by_races = BooleanProperty(False)
    end_by_time = BooleanProperty(False)

    # races
    number_of_races = NumericProperty(0)
    races_finished = NumericProperty(0)
    races_to_go = NumericProperty(0)
    race_number = NumericProperty(1)
    race_winner = ObjectProperty(None, allownone=True)
    
    # time 
    time_set_delta = timedelta()  # duration
    time_set = StringProperty('') # string representation of duration
   
    time_elapsed_delta = timedelta()   # duration
    time_elapsed = StringProperty('')  # string representation of duration
  
    time_remaining_delta = timedelta()   # duration
    time_remaining = StringProperty('')  # string representation of duration

    # callback methods
    def on_number_of_players(self, instance, value):
        if self.number_of_players == 1:
            self.players = [self.player1]
        elif self.number_of_players == 2:
            self.players = [self.player1, self.player2]
        elif self.number_of_players == 3:
            self.players = [self.player1, self.player2, self.player3]
        elif self.number_of_players == 4:
            self.players = [self.player1, self.player2, self.player3, self.player4]

    def set_ending_condition(self, condition):
        if condition == 'money':
            self.end_by_money = True
            self.end_by_races = False
            self.end_by_time = False            
        elif condition == 'races':
            self.end_by_money = False
            self.end_by_races = True
            self.end_by_time = False
        elif condition == 'time':
            self.end_by_money = False
            self.end_by_races = False
            self.end_by_time = True

    def start_game(self):
        print('Game started')

    def go(self):
        self.race_winner = choice(self.slugs)

        for player in self.players:
            player.update(self.race_winner)   

        for slug in self.slugs:
            slug.update(self.race_winner, self.race_number) 

        # Bankrupt players should be removed 
        # from the players list.
        self.remove_bankrupt_players()

    # Here's the method that removes bankrupt players from the players list.
    def remove_bankrupt_players(self):
        # Technically, the method creates a new list that contains just the players
        # who are not bankrupt. We're using a list comprehension to do that.
        # Then the new list is assigned to the players list.
        self.players = [player for player in self.players if not player.bankrupt]

    def reset_race(self):
        self.race_number += 1  

        for player in self.players:
            player.reset()

        self.race_winner = None   

class SlugraceApp(App):
    # General Settings
    initial_money_min = 10
    initial_money_max = 5000
    max_name_length = 10

    def build(self):
        return Game()

if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = (1, 1, .8, 1)
    SlugraceApp().run()
