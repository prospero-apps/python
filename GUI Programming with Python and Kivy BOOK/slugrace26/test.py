# File name: test.py

from kivy.app import App

# We must import the PageLayout class.
from kivy.uix.pagelayout import PageLayout

class TestApp(App):
    def build(self):
        # We're going to use the PageLayout now.
        return PageLayout()

if __name__ == '__main__':
    TestApp().run()

