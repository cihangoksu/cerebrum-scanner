from kivy.uix.screenmanager import Screen
from kivy.properties import (
    ObjectProperty, StringProperty, ListProperty
)

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.image import Image as CoreImage
from kivy.graphics.texture import Texture

from lib import popups

from kivy.clock import Clock
from kivy.factory import Factory

from os.path import expanduser

import io
import os
import json
from zipfile import ZipFile
import json
import csv

from kivy.logger import Logger # log files can be found in .kivy folder
Window.softinput_mode = "below_target"

def new_folders_first(files, filesystem):    
    return (sorted(f for f in files if filesystem.is_dir(f)) +
        sorted((f for f in files if not filesystem.is_dir(f)), key=lambda fi: os.stat(fi).st_mtime, reverse = True))

class ViewWindow(Screen):
    id_username = StringProperty('')
    source_image_path = StringProperty('assets/images/PNG/noImageSelected.png')
    
    def __init__(self, **kwargs):
        super(ViewWindow, self).__init__(**kwargs)
        
        from _global_paths import __path_dict__
        self.__path_dict__ = __path_dict__

        self.patient_info = {}
        self.cs_output = {}

    def Callback_Button_Enable_AI(self, *_):
        pass
        if self.cs_output['CS-ICH'] == 0: self.ids['id_AI_Diagnosis'].text = 'Hemorrhage suspected'
        elif self.cs_output['CS-ICH'] == 1: self.ids['id_AI_Diagnosis'].text = 'No hemorrhage suspected'
        else: pass

    def Callback_Button_Upload_Feedback(self, *_):
        
        feedback = {}
        feedback['CS-ICH'] = self.ids['id_Diagnosis'].text
        case_path = os.path.join(self.__path_dict__['dot-cerebrum-scanner-completed'], self.patient_info['ID'])
        with open(os.path.join(case_path,'feedback.json'), 'w') as out_file:
            json.dump(feedback, out_file)

        self.feedbacksentpopup = popups.AllWellPopup(id_AllWellPopupContent="[b]Your feedback has been sent successfully.[/b]")
        self.feedbacksentpopup.ids["id_AllWellOKButton"].bind(on_release=self.feedbacksentpopup.dismiss)
        self.feedbacksentpopup.open()


