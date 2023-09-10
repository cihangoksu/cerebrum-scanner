from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from kivy.properties import StringProperty

import json
import csv
import os

from lib import popups

class LoadingWindow(Screen):
    from _version import __version__

    id_loading_info_text = StringProperty()
    id_footer = f"© 2023 Cerebrum Scanner - Hospital. CS-Hospital-{__version__}. All rights reserved."

    assets_path = StringProperty('')

    def __init__(self, **kwargs):
        super(LoadingWindow, self).__init__(**kwargs)
        self.id_loading_info_text = "Loading... Please wait!"

        from _paths import __path_dict__        
        self.assets_path = '{}'.format(__path_dict__['common-assets'])
        
        self.finished_event = None
        
        # Clock.schedule_once(self.import_libs, 0.5)
        self.clck_trig = Clock.schedule_interval(self.trigger_events, 0.5)
        Clock.schedule_once(self.import_popups_and_paths, 0.5)

    def trigger_events(self, *_):
        # from lib import popups, browsewindow, transcribewindow, actionwindow, downloadwindow, classesforwindows
        if self.finished_event == 'popups': 
            self.finished_event = None
            self.import_browse_window()
        elif self.finished_event == 'browse': 
            self.finished_event = None
            self.GoToBrowseScreen()
        else: pass

    def import_popups_and_paths(self,*_):
        from lib import popups
        self.id_loading_info_text = "Popups and paths have been imported. Please wait..."
        self.finished_event = 'popups'


    def import_browse_window(self,*_):
        from lib import common_classes
        from lib import browsewindow
        self.manager.add_widget(browsewindow.BrowseWindow(name='browseScreen'))

        self.id_loading_info_text = "Browse menu have been imported. Please wait..."
        self.finished_event = 'browse'



    def GoToBrowseScreen(self, *_):
        self.manager.current = 'browseScreen'
        browseScreen = self.manager.get_screen('browseScreen')
        # setting the footers

        browseScreen.ids['id_footer'].text = self.id_footer