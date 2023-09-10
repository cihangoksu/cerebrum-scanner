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
    id_footer = f"© 2023 Cerebrum Scanner. CS-Team-{__version__}. All rights reserved."

    def __init__(self, **kwargs):
        super(LoadingWindow, self).__init__(**kwargs)
        from _global_paths import __path_dict__
        self.__path_dict__ = __path_dict__
        
        self.id_loading_info_text = "Loading... Please wait!"

        self.patient_info = {}
        self.case_id = ''
        self.case_path = ''
        
        self.finished_event = None
        
        # Clock.schedule_once(self.import_libs, 0.5)
        self.clck_trig = Clock.schedule_interval(self.trigger_events, 0.5)
        Clock.schedule_once(self.import_popups_and_paths, 0.5)

    def trigger_events(self, *_):
        # from lib import popups, browsewindow, transcribewindow, actionwindow, downloadwindow, classesforwindows
        if self.finished_event == 'popups': 
            self.finished_event = None
            self.import_view_window()
        elif self.finished_event == 'view': 
            self.finished_event = None
            self.bringCaseIDTextInput()
        else: pass

    def import_popups_and_paths(self,*_):
        from lib import popups
        self.id_loading_info_text = "Popups and paths have been imported. Please wait..."
        self.finished_event = 'popups'


    def import_view_window(self,*_):
        from . import common_classes
        from lib import viewwindow
        self.manager.add_widget(viewwindow.ViewWindow(name='viewScreen'))

        self.id_loading_info_text = "View menu have been imported. Please wait..."
        self.finished_event = 'view'



    def bringCaseIDTextInput(self, *_):
        self.id_loading_info_text = ""
        self.ids['id_PatientID'].disabled = False
        self.ids['id_PatientIDLabel'].disabled = False
        self.ids['id_ProceedViewWindow'].disabled = False

    def Callback_Proceed(self, *_): 
        self.case_id = self.ids['id_PatientID'].text
        self.case_path = os.path.join(self.__path_dict__['dot-cerebrum-scanner-completed'], self.case_id)
        self.GoToViewScreen()


    def GoToViewScreen(self, *_):
        viewScreen = self.manager.get_screen('viewScreen')
        png_path = os.path.join(self.case_path,f'{self.case_id}.png')
        viewScreen.source_image_path = png_path
        
        with open(os.path.join(self.case_path,f'{self.case_id}.json')) as out_file:
            patient_info_json = json.load(out_file)
        viewScreen.patient_info = patient_info_json
        
        with open(os.path.join(self.case_path,'cs-output.json')) as out_file:
            cs_output = json.load(out_file)
        viewScreen.cs_output = cs_output
        
        # setting the footers

        {"ID": "X12345", "AGE": "32", "SEX": "m", "SYMPTOM_ONSET": "96", "NIHSS": "6", "MRS": "2"}
        viewScreen.ids['id_ScanPathInfo'].text = f'{patient_info_json["AGE"]}y({patient_info_json["SEX"]}). Onset {patient_info_json["SYMPTOM_ONSET"]} mins, NIHSS = {patient_info_json["NIHSS"]}, MRS = {patient_info_json["MRS"]}.'
        viewScreen.ids['id_footer'].text = self.id_footer
        self.manager.current = 'viewScreen'