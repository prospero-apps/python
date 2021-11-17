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

        self.remove_bankrupt_players()
        self.gameover_check()

    def remove_bankrupt_players(self):
        self.players = [player for player in self.players if not player.bankrupt]

    # Let's simplify the gameover_check method so that it only checks whether the game 
    # should be over and calls the gameover method if so. The actual handling of ending 
    # the game is moved to the gameover method.
    def gameover_check(self):
        # The game should be over if:
        # - there are no more players in the game,
        # - there's only one player with money and we're in multi-player mode,
        # - the game should end after a specific number of races and this number
        #   has just been reached.
        if (len(self.players) == 0
            or (len(self.players) == 1 and self.number_of_players > 1)
            or (self.end_by_races and self.race_number == self.number_of_races)):
            self.gameover()

    # This is the method that handles the end of the game.
    def gameover(self):
        # Clear the winners list.
        self.winners = []

        # The game is over regardless of the ending condition as soon as all players 
        # go bankrupt. Depending on whether there was only one player or more at the 
        # beginning of the game, the messages in the Game Over screen will be different.
        if len(self.players) == 0:

            # 1-player mode
            if self.number_of_players == 1:
                self.game_over_reason = 'You just went bankrupt.'
                self.winner_text = 'There are no winners in 1-player mode.'

            # multi-player mode
            else:
                self.game_over_reason = 'All players are bankrupt.' 
                self.winner_text = 'There is no winner!'

        # If there are multiple players, the game should be over always when there's 
        # only one player with any money left, regardless of the ending condition. Then
        # this one player is appended to the winners list and is the only winner.
        elif len(self.players) == 1 and self.number_of_players > 1:
            self.winners.append(self.players[0])
            self.game_over_reason = "There's only one player with any money left." 
            winner = self.winners[0]
            self.winner_text = (f'The winner is {winner.name}, ' + 
                                f'having started at ${winner.initial_money}, ' + 
                                f'winning at ${winner.money}.')
        
        # If none of the conditions above is met, so if there is more than one player 
        # still in the game or if we're in 1-player mode, the next condition to check 
        # is whether the ending condition is end_by_races. If so, we must check whether 
        # the number of the last race is equal to the number of races we set. If it is, 
        # the game should be over.
        elif self.end_by_races and self.race_number == self.number_of_races:

            # The game over reason text should be the same regardless of the number of 
            # players. One exception is when there's only one player left because then 
            # the condition above will be checked before the condition over here, which 
            # means the message "There's only one player with any money left." will be 
            # displayed. In other cases, so if more than one player is still in the game 
            # or if we're in 1-player mode, the message below will be shown.           
            self.game_over_reason = 'The number of races you set has been reached.'
            
            # There is no winner in 1-player mode, so we just see some general info text 
            # about how the player did in the game.
            if self.number_of_players == 1:
                you = self.players[0]
                self.winner_text = (f"You were playing in 1-player mode." + 
                                    f"\nYou started at ${you.initial_money} " + 
                                    f"and you're ending at ${you.money}.")
               
            # If there is more than one player with money left, the result depends on 
            # how much money the players have. If there is one player with more money 
            # than any other player, he or she is the winner. But if there are two or 
            # more players with the same maximum amount of money, we have a tie and all 
            # these players are joint winners.
            else:

                # First we must find the winner or winners. Let's start by figuring out 
                # what is the maximum amount of money that any player has. We can use 
                # the Python built-in max function to do that. Besides the unpacked 
                # (hence the star operator) list of players, we pass the key argument to 
                # tell the function by which criterion to search for the maximum value. 
                # Here we're using a simple lambda function to tell the function to 
                # search through the players list by money. So, the max function finds
                # the player with the maximum amount of money (or the first such player 
                # if there are more). Then the money of the player found by max is 
                # assigned to max_money.
                max_money = (max(*self.players, key=lambda player: player.money)).money
                
                # Now we know what the maximum amount of money is. We can now re-create
                # the list of winners using a list comprehension where all players are
                # placed who have the maximum amount of money. This list may contain
                # just one player, or more if there is more than one player with the
                # maximum amount of money.
                self.winners = [player for player in self.players 
                                if player.money == max_money]

                # Now we must display a different message depending on whether there is
                # one winner or more. 

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
               
        # Switch to Gameover screen.
        self.current = 'gameoverscreen'  
      
    def reset_race(self):
        self.race_number += 1 
        self.races_finished += 1
        self.races_to_go -= 1     

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
