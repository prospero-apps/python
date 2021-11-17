# File name: splash.py

from kivy.uix.screenmanager import Screen, FadeTransition, SlideTransition
from kivy.clock import Clock

class SplashScreen(Screen):
    def on_enter(self):
        # Call the move_on method in 5 seconds.        
        Clock.schedule_once(self.move_on, 5)   

    def move_on(self, dt):
        # Change transition type to FadeTransition and switch to Settings screen.
        self.game.transition = FadeTransition()
        self.game.current = 'settingsscreen'

    def on_leave(self):
        # On leaving the Splash screen change the transition type back to
        # SlideTransition so that we don't have the FadeTransition everywhere.
        self.game.transition = SlideTransition()
