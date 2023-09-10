# by Nekodu Technology Inc.
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.text import LabelBase
from kivy.core.window import Window
Window.maximize()

from kivy.base import runTouchApp

from _global_paths import __path_dict__
import os

from lib import loadingwindow

# Create the screen manager
Builder.load_file(os.path.join(__path_dict__['kvfiles'],"loadingwindow.kv"))
Builder.load_file(os.path.join(__path_dict__['kvfiles'],"viewwindow.kv"))
Builder.load_file(os.path.join(__path_dict__['kvfiles'],"common_classes.kv"))

sm = ScreenManager(transition=FadeTransition())
from lib import common_classes
sm.add_widget(loadingwindow.LoadingWindow(name='loadingScreen'))

class csNeurologistMainApp(App):
    def build(self): return sm

if __name__ == '__main__':
    csNeurologistMainApp().run()
