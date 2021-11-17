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
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout

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
    potential_players = [player1, player2, player3, player4]

    # ending conditions
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

    # game over
    winners = []
    game_over_reason = StringProperty('')
    winner_text = StringProperty('') 
    game_is_over = BooleanProperty(False)     

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
        if self.end_by_time:
            self.time_event = Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        # Add one second to elapsed time.
        self.time_elapsed_delta += timedelta(seconds=1)
        self.time_elapsed = str(self.time_elapsed_delta)

        # Subtract one second from remaining time.
        self.time_remaining_delta -= timedelta(seconds=1)
        self.time_remaining = str(self.time_remaining_delta)

        # Unschedule the update_time method if the time has elepased.
        if self.time_remaining_delta.seconds == 0:
            self.time_event.cancel()

            self.gameover()

    def go(self):
        self.race_winner = choice(self.slugs)

        for player in self.players:
            player.update(self.race_winner)   

        for slug in self.slugs:
            slug.update(self.race_winner, self.race_number) 

        self.remove_bankrupt_players()
        self.gameover_check()

    def remove_bankrupt_players(self):
        self.players = [player for player in self.players if not player.bankrupt]

    def gameover_check(self):
        if (len(self.players) == 0
            or (len(self.players) == 1 and self.number_of_players > 1)
            or (self.end_by_races and self.race_number == self.number_of_races)
            or (self.end_by_time and self.time_remaining_delta.seconds == 0)):
            self.gameover()

    def gameover(self):
        self.winners = []

        if len(self.players) == 0:

            # 1-player mode
            if self.number_of_players == 1:
                self.game_over_reason = 'You just went bankrupt.'
                self.winner_text = 'There are no winners in 1-player mode.'

            # multi-player mode
            else:
                self.game_over_reason = 'All players are bankrupt.' 
                self.winner_text = 'There is no winner!'

        elif len(self.players) == 1 and self.number_of_players > 1:
            self.winners.append(self.players[0])
            self.game_over_reason = "There's only one player with any money left." 
            winner = self.winners[0]
            self.winner_text = (f'The winner is {winner.name}, ' + 
                                f'having started at ${winner.initial_money}, ' + 
                                f'winning at ${winner.money}.')
        
        # after a given number of races or after the game time has elapsed
        elif ((self.end_by_races and self.race_number == self.number_of_races)
              or (self.end_by_time and self.time_remaining_delta.seconds == 0)):

            self.game_over_reason = ('The number of races you set has been reached.' 
                if self.end_by_races else 'The game time you set is up.')
            
            if self.number_of_players == 1:
                you = self.players[0]
                self.winner_text = (f"You were playing in 1-player mode." + 
                                    f"\nYou started at ${you.initial_money} " + 
                                    f"and you're ending at ${you.money}.")
               
            else:
                max_money = (max(*self.players, key=lambda player: player.money)).money                
                self.winners = [player for player in self.players 
                                if player.money == max_money]

                # one winner
                if len(self.winners) == 1:
                    winner = self.winners[0]
                    self.winner_text = (f'The winner is {winner.name}, ' + 
                                       f'having started at ${winner.initial_money}, ' + 
                                       f'winning at ${winner.money}.')
                
                # joint winners
                else:
                    self.winner_text = "There's a tie. The joint winners are:\n\n"
                    for winner in self.winners:                        
                        self.winner_text += (f'{winner.name}, ' + 
                                            f'having started at ${winner.initial_money}, ' + 
                                            f'winning at ${winner.money}.\n')
                
        self.game_is_over = True        
        self.gameover_event = Clock.schedule_once(self.gameover_screen, 4)
      
    def gameover_screen(self, dt):
        self.current = 'gameoverscreen'
        self.gameover_event.cancel()
  
    def reset_race(self):
        self.race_number += 1 
        self.races_finished += 1
        self.races_to_go -= 1     

        for player in self.players:
            player.reset()

        self.race_winner = None   
    
    def reset_players(self):
        for player in self.potential_players:
            player.reset(gameover = True)

class SlugraceApp(App):
    # General Settings
    initial_money_min = 10
    initial_money_max = 5000
    max_name_length = 10

    def restart(self):
        self.root.clear_widgets()
        
        # Let's create a Game instance and assign it to a variable.
        self.game = Game()

        # Let's make the Game widget fully transparent.
        self.game.opacity = 0

        # Let's add the Game instance to the root widget.
        self.root.add_widget(self.game)

        # Let's schedule the show method to be called every 0.01 seconds.
        self.show_event = Clock.schedule_interval(self.show, .01)
               
    # Here's the show method. 
    def show(self, dt):
        # It increases the opacity by 0.01.
        self.game.opacity += .01

        # If the opacity is 1 or more...
        if self.game.opacity >= 1:

            # ...it's set to exactly 1 and...
            self.game.opacity = 1

            # ... the method is unscheduled.
            self.show_event.cancel()

    def build(self):
        self.root = FloatLayout()
        self.root.add_widget(Game())
        return self.root

if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = (1, 1, .8, 1)
    SlugraceApp().run()
