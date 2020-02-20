# We're using Kivy, so we'll need the kivy module
import kivy

# We need the App class. Our application is going to inherit from it.
from kivy.app import App

# We also need the Label widget.
from kivy.uix.button import Label

# Here comes the application class. It inherits from App.
class HelloWorldApp(App):
    def build(self):
        return Label(text='Hello World!')

# And this is where we actually run the app.
if __name__ == '__main__':
    HelloWorldApp().run()