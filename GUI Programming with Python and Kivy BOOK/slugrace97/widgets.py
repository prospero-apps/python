# File name: widgets.py

from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.properties import NumericProperty

class NameInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    def insert_text(self, substring, from_undo=False):  
        if len(self.text + substring) <= self.app.max_name_length:              
            return super(NameInput, self).insert_text(substring, from_undo = from_undo)

    # This method will set the cursor 
    # width to 1.01 when the text input 
    # gets focus and there is no text 
    # in it.
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

    # Here we already have the code used to 
    # validate the text, which we must keep.
    # The validation code is executed when 
    # the widget loses focus, so we can add
    # an else block for the code that sets 
    # the cursor width.
    def on_focus(self, instance, value):
        if not value:
            self.on_text_validate()
        else: 
            if self.text == '':
                self.cursor_width = 1.01
