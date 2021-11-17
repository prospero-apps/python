# File name: test.py

# We need the App class. Our application is going to inherit from it.
from kivy.app import App

# We also need the Label widget.
from kivy.uix.label import Label

# Here comes the application class. It inherits from App. 
class TestApp(App):
    def build(self):
        # A label is returned.
        return Label(text='Hello World!')

# And this is where we actually run the app.
if __name__ == '__main__':
    TestApp().run()