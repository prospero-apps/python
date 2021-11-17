# File name: widgets.py

from kivy.uix.textinput import TextInput
from kivy.app import App

# We'll need the StringProperty class as well.
from kivy.properties import NumericProperty, StringProperty

# We'll need the ToggleButton class to inherit from.
from kivy.uix.togglebutton import ToggleButton

class NameInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    def insert_text(self, substring, from_undo=False):  
        if len(self.text + substring) <= self.app.max_name_length:              
            return super(NameInput, self).insert_text(substring, from_undo = from_undo)

    def on_focus(self, instance, value):
        if value and self.text == '':
            self.cursor_width = 1.01

class NumInput(TextInput):
    min_value = NumericProperty()
    max_value = NumericProperty()    

    def insert_text(self, substring, from_undo=False):             
        return (super().insert_text(substring, from_undo=from_undo) if substring != '-' 
                else super().insert_text('', from_undo=from_undo))

    def on_text_validate(self):
        if self.text:
            self.text = str(max(self.min_value, min(int(self.text), self.max_value)))

    def on_focus(self, instance, value):
        if not value:
            self.on_text_validate()
        else: 
            if self.text == '':
                self.cursor_width = 1.01
            
# Here's the SoundButton class that inherits from ToggleButton.
# It contains the image_source StringProperty.
class SoundButton(ToggleButton):
    image_source = StringProperty('')

