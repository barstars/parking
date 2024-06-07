from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder

class Where_are_you(Screen):
	pass

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.transition = NoTransition()

class Parking(App):
    def build(self):
        return WindowManager()

if __name__ == '__main__':
	Parking().run()