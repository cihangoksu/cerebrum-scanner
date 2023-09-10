# by Nekodu Technology Inc.
from gestures4kivy import CommonGestures
from kivy.config import Config
Config.set('input', 'mouse', 'mouse, disable_multitouch')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.text import LabelBase
from kivy.core.window import Window
Window.maximize()

from kivy.base import runTouchApp

from _paths import __path_dict__
import os

from lib import loadingwindow

# Create the screen manager
Builder.load_file(os.path.join(__path_dict__['kvfiles'],"loadingwindow.kv"))
Builder.load_file(os.path.join(__path_dict__['kvfiles'],"browsewindow.kv"))
Builder.load_file(os.path.join(__path_dict__['kvfiles'],"common_classes.kv"))

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(loadingwindow.LoadingWindow(name='loadingScreen'))

class csORGMainApp(App):
    def build(self): 
        self.assets_path = __path_dict__
        return sm

if __name__ == '__main__':
    csORGMainApp().run()
