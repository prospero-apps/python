# File name: test.py

from kivy.app import App
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_string("""
<TextInput>: 
    text: '1\\n2\\n3'   
    hint_text: 'Add some numbers...'
    background_color: [.5, .5, .5, 1]
    foreground_color: [.8, .8, .8, 1]
    hint_text_color: [.2, .2, .2, 1]
    font_size: 60
    halign: 'center'
""")

class TestApp(App):
    def build(self):
        return TextInput()

if __name__ == '__main__':
    TestApp().run()
