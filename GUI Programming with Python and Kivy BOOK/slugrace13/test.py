# File name: test.py

from kivy.app import App
from kivy.uix.switch import Switch

sw = Switch(active=True)

# Let's define the callback functions.
def down_callback(instance, value):
    print('*****')

def active_callback(instance, value):
    if value:
        print('activated')
    else:
        print('deactivated')

# Let's bind the events to the callback functions.
sw.bind(on_touch_down=down_callback)
sw.bind(active=active_callback)

class TestApp(App):
    def build(self):
        return sw

if __name__ == '__main__':
    TestApp().run()