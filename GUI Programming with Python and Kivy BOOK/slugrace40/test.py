# File name: test.py

from kivy.app import App

# our imports
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

# Let's define the BigButton and SmallButton 
# classes that inherit from Button.
class BigButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (200, 200)

class SmallButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (100, 100)

# Let's define the OuterGridLayout class 
# that inherits from GridLayout.
class OuterGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 3
        self.size_hint = (None, None)
        self.size = (600, 600)

# Let's create the outer layout.
main_layout = OuterGridLayout()

# Let's create the two inner GridLayouts.
inner_layout1 = GridLayout(rows=2)
inner_layout2 = GridLayout(rows=2)

# Let's add the small buttons to the inner layouts.
labels1 = ['4a', '4b', '4c', '4d']
for label in labels1:
    inner_layout1.add_widget(Button(text=label))

labels2 = ['9a', '9b', '9c', '9d']
for label in labels2:
    inner_layout2.add_widget(Button(text=label))

# Let's add the big buttons and the inner 
# layouts to the outer layout.
main_layout.add_widget(BigButton(text='1'))
main_layout.add_widget(BigButton(text='2'))
main_layout.add_widget(BigButton(text='3'))
main_layout.add_widget(inner_layout1)
main_layout.add_widget(BigButton(text='5'))
main_layout.add_widget(BigButton(text='6'))
main_layout.add_widget(BigButton(text='7'))
main_layout.add_widget(BigButton(text='8'))
main_layout.add_widget(inner_layout2)

class TestApp(App):
    def build(self):
        return main_layout

if __name__ == '__main__':
    TestApp().run()
