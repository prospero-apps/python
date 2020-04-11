import kivy
from kivy.app import App

# We must import the AnchorLayout class.
from kivy.uix.anchorlayout import AnchorLayout

class HelloWorldApp(App):
    def build(self):
        # We're going to use the AnchorLayout now.
        return AnchorLayout()

if __name__ == '__main__':
    HelloWorldApp().run()
