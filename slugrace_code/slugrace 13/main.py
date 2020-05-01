import kivy
from kivy.app import App

# We need a GridLayout to embed the other GridLayouts into.
from kivy.uix.gridlayout import GridLayout

# Let's create a custom GridLayout to act as the outer container.
class OuterGridLayout(GridLayout):
    pass

class HelloWorldApp(App):
    def build(self):
        return OuterGridLayout()

if __name__ == '__main__':
    HelloWorldApp().run()
