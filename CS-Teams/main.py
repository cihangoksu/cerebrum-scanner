# by Nekodu Technology Inc.
from gestures4kivy import CommonGestures
from kivy.config import Config
Config.set('input', 'mouse', 'mouse, disable_multitouch')

from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.text import LabelBase
from kivy.core.window import Window
Window.size = 360,640

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

class csTEAMSMainApp(MDApp):
    def build(self): 
        self.assets_path = __path_dict__
        
        self.window_width, self.window_height= Window.size

        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        
        return sm

if __name__ == '__main__':
    csTEAMSMainApp().run()
