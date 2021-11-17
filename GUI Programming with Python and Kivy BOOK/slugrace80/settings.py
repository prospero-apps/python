# File name: settings.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

class PlayerCount(BoxLayout):
    count_text = StringProperty('')

class PlayerSettings(BoxLayout):
    label_text = StringProperty('')

class SettingsScreen(Screen):
    # Here's the method used for the players settings. 
    def set_players(self, players):
        # Let's import the App class and call the get_running_app method.        
        from kivy.app import App
        app = App.get_running_app()

        # Let's iterate over the players.
        for i, player in enumerate(self.game.players):

            # First let's set each player's name. 
            player.name = 'Player ' + str(i + 1) if not players[i].name else players[i].name

            # Now let's set the player's initial money. 
            player.initial_money = (1000 if not players[i].player_initial_money 
                else max(app.initial_money_min, 
                    min(int(players[i].player_initial_money), app.initial_money_max)))

            # When the game begins, a player's money is the same as their initial money. 
            player.money = player.initial_money   
