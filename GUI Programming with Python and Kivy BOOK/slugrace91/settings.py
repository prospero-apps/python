# File name: settings.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen 
from random import randint
from datetime import timedelta

class PlayerCount(BoxLayout):
    count_text = StringProperty('')

class PlayerSettings(BoxLayout):
    label_text = StringProperty('')

class SettingsScreen(Screen):
    def set_players(self, players):       
        from kivy.app import App
        app = App.get_running_app()

        for i, player in enumerate(self.game.players):
            player.name = 'Player ' + str(i + 1) if not players[i].name else players[i].name
            player.initial_money = (1000 if not players[i].player_initial_money 
                else max(app.initial_money_min, 
                    min(int(players[i].player_initial_money), app.initial_money_max)))
            player.money = player.initial_money   

    def set_slugs(self):        
        self.game.speedster.wins = 0
        self.game.speedster.win_percent = 0.00
        self.game.speedster.odds = round(1.33 + randint(0, 10) / 100, 2) 
  
        self.game.trusty.wins = 0
        self.game.trusty.win_percent = 0.00
        self.game.trusty.odds = round(1.59 + randint(0, 10) / 100, 2) 
  
        self.game.iffy.wins = 0
        self.game.iffy.win_percent = 0.00
        self.game.iffy.odds = round(2.5 + randint(0, 10) / 100, 2) 
     
        self.game.slowpoke.wins = 0
        self.game.slowpoke.win_percent = 0.00
        self.game.slowpoke.odds = round(2.89 + randint(0, 10) / 100, 2) 

    def set_game(self, number_of_races, time_set):
        if number_of_races != '':
            self.game.number_of_races = int(number_of_races) 
            self.game.races_to_go = self.game.number_of_races                             

        if time_set != '': 
            self.game.time_set_delta = timedelta(minutes = int(time_set)) 
            self.game.time_set = str(self.game.time_set_delta)
            self.game.time_elapsed = str(self.game.time_elapsed_delta)
            self.game.time_remaining_delta = self.game.time_set_delta
            self.game.time_remaining = str(self.game.time_remaining_delta)

    # The method will make the widgets passed as arguments lose focus.
    def defocus(self, *widgets):
        for widget in widgets:
            widget.focus = False

