# File name: test.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '1')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class TestLayout(FloatLayout):
    pass

class CustomButton(Button):
    def set_text(self):
        # variables used for better readability
        root = self.parent
        label1 = root.children[-1]
        button1 = root.children[2].children[-1]
        button2 = root.children[2].children[1].children[-1]
        slider = root.children[2].children[1].children[1]
        button3 = root.children[2].children[1].children[0]
        button4 = root.children[2].children[0]
        button5 = self
        label2 = root.children[0]

        ### set the text on the first label
        label1.text = str(type(label1))

        ### set the text on the first button
        button1.text = str(slider.orientation)

        ### set the text on the second button
        button2.text = str(slider.value)

        ### set the text on the third button
        button3.text = str(button3.parent.parent.parent == root)

        ### set the text on the fourth button
        button4.text = str(len(root.children))

        ### set the text on this very button
        button5.text = str(root.children.index(self))

        ### set the text on the second label
        label2.text = 'yes' if label2 in root.children else 'no'     

class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()
