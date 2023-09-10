from kivy.uix.screenmanager import Screen
from kivy.properties import (
    ObjectProperty, StringProperty, ListProperty, NumericProperty
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


from lib import imageprocessor
clIMAGEPROCESSOR = imageprocessor.ImageProcessor()

import client
clCLIENT = client.Client()

from gestures4kivy import CommonGestures

from PIL import Image
import numpy as np
import copy

def new_folders_first(files, filesystem):    
    return (sorted(f for f in files if filesystem.is_dir(f)) +
        sorted((f for f in files if not filesystem.is_dir(f)), key=lambda fi: os.stat(fi).st_mtime, reverse = True))

class BrowseWindow(Screen, CommonGestures):
    id_username = StringProperty('')
    assets_path = StringProperty('')

    selected_scan_name = StringProperty()
    
    scale_factor_size = NumericProperty(1)

    ct_Image_level = NumericProperty(30)
    ct_Image_width = NumericProperty(70)

    texture_CTScanScatterImage = ObjectProperty()

    
    number_msg = NumericProperty(0)

    def __init__(self, **kwargs):
        super(BrowseWindow, self).__init__(**kwargs)
        
        from _paths import __path_dict__        
        self.assets_path = '{}'.format(__path_dict__['common-assets'])
        self.__path_dict__ = __path_dict__

        self.target_PACS_folder_path = self.__path_dict__['dot-cerebrum-scanner-data']



        self.patient_info = {}

        self.scale_factor_size_upper_limit = 1.3
        self.scale_factor_size_lower_limit = 0.5

        self.nifti_file_paths_list = []
        self.selected_scan_nifti_folder = None

        self.selected_scan_name = 'scan name'
        self.selected_scan_index = 0
        self.scan_names_list = []

        self.brain_vol = None
        self.selected_slice = 0

        self.clock_texture_update = None


    def on_enter(self, *args):
        self.ids['id_CTScanScatterImage'].pos[0] = Window.width*self.ids['id_BoxLayoutScatter'].pos_hint['center_x'] - self.ids['id_CTScanScatterImage'].size[0]*0.5
        self.ids['id_CTScanScatterImage'].pos[1] = Window.height*self.ids['id_BoxLayoutScatter'].pos_hint['center_y'] - self.ids['id_CTScanScatterImage'].size[1]*0.5

        self.ids['id_CTScanScatterImage'].opacity= 1

        
        self.ids['id_TextInputWindow_width'].text = str(self.ct_Image_width)
        self.ids['id_TextInputWindow_level'].text = str(self.ct_Image_level)




        #### DELeTE THIS####3
        self.ids['id_PatientID'].text = 'X12345'
        self.ids['id_PatientAge'].text = '23'
        self.ids['id_PatientSex'].text = 'f'
        self.ids['id_PatientSymptomOnset'].text = '88'
        self.ids['id_PatientNIHSS'].text = '4'
        self.ids['id_PatientMRS'].text = '6'



        return super().on_enter(*args)
        
        



    def cgb_zoom(self, touch0, touch1, focus_x, focus_y, delta_scale):
        
        # import pdb; pdb.set_trace()
        x0, y0 = self.ids['id_CTScanScatterImage'].pos[0], self.ids['id_CTScanScatterImage'].pos[1]
        dx, dy = touch0.x - x0, touch0.y - y0

        if self.scale_factor_size<=self.scale_factor_size_upper_limit: 

            if self.scale_factor_size>=self.scale_factor_size_lower_limit: 
                self.scale_factor_size += -1+delta_scale

                self.ids['id_CTScanScatterImage'].pos[0] += (1 - delta_scale)*dx
                self.ids['id_CTScanScatterImage'].pos[1] += (1 - delta_scale)*dy

            else:
                if delta_scale>1: 
                    self.scale_factor_size = self.scale_factor_size_lower_limit -1 + delta_scale

                    self.ids['id_CTScanScatterImage'].pos[0] += (1 - delta_scale)*dx
                    self.ids['id_CTScanScatterImage'].pos[1] += (1 - delta_scale)*dy

        else:
            if  delta_scale<1: 
                self.scale_factor_size = self.scale_factor_size_upper_limit -1 + delta_scale

                self.ids['id_CTScanScatterImage'].pos[0] += (1 - delta_scale)*dx
                self.ids['id_CTScanScatterImage'].pos[1] += (1 - delta_scale)*dy


        
        self.ids['id_CTScanScatterImage'].opacity= 0
        self.ids['id_CTScanScatterImage'].opacity= 1
        # import pdb; pdb.set_trace()



    def cgb_drag(self, touch, focus_x, focus_y, delta_x, delta_y):
        # drag behaviour within the Float Layout
        if (touch.x > self.ids['id_CTScanScatterImage'].pos[0] and touch.x < self.ids['id_CTScanScatterImage'].pos[0]+self.ids['id_CTScanScatterImage'].size[0]
            and touch.y > self.ids['id_CTScanScatterImage'].pos[1] and touch.y < self.ids['id_CTScanScatterImage'].pos[1]+self.ids['id_CTScanScatterImage'].size[1]):
            self.ids['id_CTScanScatterImage'].pos[0] += delta_x 
            self.ids['id_CTScanScatterImage'].pos[1] += delta_y
        
        if self.ids['id_CTScanScatterImage'].center[0] < self.ids['id_BoxLayoutScatter'].pos[0]:
            self.ids['id_CTScanScatterImage'].pos[0] = self.ids['id_BoxLayoutScatter'].pos[0] - self.ids['id_CTScanScatterImage'].size[0]*0.5
        if self.ids['id_CTScanScatterImage'].center[0] > self.ids['id_BoxLayoutScatter'].pos[0] + self.ids['id_BoxLayoutScatter'].size[0]:
            self.ids['id_CTScanScatterImage'].pos[0] = self.ids['id_BoxLayoutScatter'].pos[0] + self.ids['id_BoxLayoutScatter'].size[0] - self.ids['id_CTScanScatterImage'].size[0]*0.5

        if self.ids['id_CTScanScatterImage'].center[1] < self.ids['id_BoxLayoutScatter'].pos[1]:
            self.ids['id_CTScanScatterImage'].pos[1] = self.ids['id_BoxLayoutScatter'].pos[1] - self.ids['id_CTScanScatterImage'].size[1]*0.5
        if self.ids['id_CTScanScatterImage'].center[1] > self.ids['id_BoxLayoutScatter'].pos[1] + self.ids['id_BoxLayoutScatter'].size[1]:
            self.ids['id_CTScanScatterImage'].pos[1] = self.ids['id_BoxLayoutScatter'].pos[1] + self.ids['id_BoxLayoutScatter'].size[1] - self.ids['id_CTScanScatterImage'].size[1]*0.5

        # self.ids['id_CTScanScatterImage'].center[1] < self.ids['id_BoxLayoutScatter'].pos[1] 
        # self.ids['id_CTScanScatterImage'].center[0] < self.ids['id_BoxLayoutScatter'].pos[0] and
        
        
        # Window.width*self.ids['id_BoxLayoutScatter'].pos_hint['center_x'] - self.ids['id_CTScanScatterImage'].size[0]*0.5
        # self.ids['id_CTScanScatterImage'].pos[1] = Window.height*self.ids['id_BoxLayoutScatter'].pos_hint['center_y'] - self.ids['id_CTScanScatterImage'].size[1]*0.5




    def cgb_select(self, touch, focus_x, focus_y, long_press):
        if self.scale_factor_size == 1:
            self.ids['id_CTScanScatterImage'].pos[0] = Window.width*self.ids['id_BoxLayoutScatter'].pos_hint['center_x'] - self.ids['id_CTScanScatterImage'].size[0]*0.5
            self.ids['id_CTScanScatterImage'].pos[1] = Window.height*self.ids['id_BoxLayoutScatter'].pos_hint['center_y'] - self.ids['id_CTScanScatterImage'].size[1]*0.5
        else:
            self.scale_factor_size = 1

        self.ids['id_CTScanScatterImage'].opacity= 1

        
        pass


    def cgb_scroll(self, touch, focus_x, focus_y, delta_y, velocity):
        num_slices = self.brain_vol.shape[2]
        if delta_y>0 and self.selected_slice<num_slices-1: self.selected_slice += 1
        elif delta_y<0 and self.selected_slice>0: self.selected_slice -= 1
        else: pass

        self.update_texture()



    def Callback_Button_Browse(self, *_):
        
        self.BrowsePopup = popups.FileBrowsePopup(id_defaultpath="", 
                                                  id_FileBrowsePopupContent="", 
                                                  id_ConvertDicomButtonContent = "dcm2nifti",
                                                  id_CancelButtonContent="", 
                                                  id_ProceedButtonContent="")
        self.BrowsePopup.id_defaultpath = self.target_PACS_folder_path
        self.BrowsePopup.id_FileBrowsePopupContent = 'Please choose the [b]Dicom folder or Nifti file[/b] you want to view.'
        self.BrowsePopup.id_CancelButtonContent = "Cancel"
        self.BrowsePopup.id_ConvertDicomButtonContent = "dcm2nifti"
        self.BrowsePopup.id_ProceedButtonContent = "Choose"
        
        self.BrowsePopup.ids['id_filechooser'].sort_func = new_folders_first
        self.BrowsePopup.ids["id_CancelButton"].bind(on_release=self.BrowsePopup.dismiss)
        self.BrowsePopup.ids["id_ConvertDicomButton"].bind(on_release=self.ConvertDicomToNifti)
        
        self.BrowsePopup.ids["id_ProceedButton"].bind(on_release=self.BrowsePopup.dismiss)
        self.BrowsePopup.ids["id_ProceedButton"].bind(on_release=self.Choose_Selected_Path)

        self.BrowsePopup.open()


        
    def ConvertDicomToNifti(self, *_):
        print('Conversion dcm2nifti is in progress...')
        self.fill_patient_info()
        dicom_folder_path = self.BrowsePopup.ids["id_filechooser"].selection[0]
        from datetime import datetime
        date_now = datetime.utcnow().strftime('%Y-%m-%d-%H-%M')
        case_name = '{}-{}'.format(self.patient_info['ID'], date_now)
        nifti_folder_path = os.path.join(self.__path_dict__['dot-cerebrum-scanner-tmp'],case_name)

        clIMAGEPROCESSOR.dicom_directory, clIMAGEPROCESSOR.output_folder = dicom_folder_path, nifti_folder_path
        clIMAGEPROCESSOR.convert_dicom_folder_to_nifti()

    def fill_patient_info(self,*_):
        self.patient_info['ID'] = self.ids['id_PatientID'].text
        if self.patient_info['ID'] == '': self.patient_info['ID'] = 'XXX'
        self.patient_info['AGE'] = self.ids['id_PatientAge'].text
        self.patient_info['SEX'] = self.ids['id_PatientSex'].text
        self.patient_info['SYMPTOM_ONSET'] = self.ids['id_PatientSymptomOnset'].text
        self.patient_info['NIHSS'] = self.ids['id_PatientNIHSS'].text
        self.patient_info['MRS'] = self.ids['id_PatientMRS'].text


    def Choose_Selected_Path(self, *_):
        self.ids['id_ScanPathInfo'].text = 'CT Scan has now been selected!'

        self.fill_patient_info()
        self.ids['id_ConsultButton'].disabled = False

        ##### Numpy check
        # Open the image form working directory
        nifti_file_path = self.BrowsePopup.ids["id_filechooser"].selection[0]
        nifti_folder_path, selected_nifti_name = os.path.split(nifti_file_path)
        self.selected_scan_name, self.selected_scan_nifti_folder = selected_nifti_name, nifti_folder_path

        self.scan_names_list = os.listdir(nifti_folder_path)
        for nifti_name in self.scan_names_list: self.nifti_file_paths_list.append(os.path.join(nifti_folder_path, nifti_name))
        # clIMAGEPROCESSOR.get_brain_vol_dict(self.nifti_file_paths_list)

        # image = clIMAGEPROCESSOR.brain_vol_dict[selected_nifti_name][:,:,15]
        
        self.selected_scan_index = self.scan_names_list.index(self.selected_scan_name)

        ############
        self.brain_vol = clIMAGEPROCESSOR.get_brain_vol(nifti_file_path)
        self.selected_slice = int(self.brain_vol.shape[2]/2)
        
        img_raw = copy.deepcopy(self.brain_vol[:,:,self.selected_slice])

        # Set color limits for the texture
        min_color = self.ct_Image_level - self.ct_Image_width/2  # Minimum color limit
        max_color = self.ct_Image_level + self.ct_Image_width/2  # Maximum color limit

        img_raw[img_raw<min_color] = min_color
        img_raw[img_raw>max_color] = max_color



        img = (img_raw - np.min(img_raw)) / (np.max(img_raw) - np.min(img_raw))

        Imagetexture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='luminance')
        Imagetexture.blit_buffer(img.astype('float32').tobytes(), colorfmt='luminance', bufferfmt='float')


        self.texture_CTScanScatterImage = Imagetexture



        self.ids['id_TextInputWindow_width'].bind(on_text_validate=self.update_texture)
        self.ids['id_TextInputWindow_level'].bind(on_text_validate=self.update_texture)

        # self.clock_texture_update = Clock.schedule_interval(self.update_texture, 1)


    def update_texture(self, *_):
        print('Texture update started')
        try:
            img_raw = copy.deepcopy(self.brain_vol[:,:,self.selected_slice])

            # Set color limits for the texture
            ct_Image_level, ct_Image_width = int(self.ids['id_TextInputWindow_level'].text), int(self.ids['id_TextInputWindow_width'].text)

            print(f'{ct_Image_width} and {ct_Image_level}')

            min_color = ct_Image_level - ct_Image_width/2  # Minimum color limit
            max_color = ct_Image_level + ct_Image_width/2  # Maximum color limit

            img_raw[img_raw<min_color] = min_color
            img_raw[img_raw>max_color] = max_color



            img = (img_raw - np.min(img_raw)) / (np.max(img_raw) - np.min(img_raw))

            Imagetexture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='luminance')
            Imagetexture.blit_buffer(img.astype('float32').tobytes(), colorfmt='luminance', bufferfmt='float')


            self.texture_CTScanScatterImage = Imagetexture


        except:
            print('Texture update failed.')
            import pdb; pdb.set_trace()


    def Callback_get_previous_scan(self, *_):
        
        if self.selected_scan_index>0: 
            self.selected_scan_index -= 1 
            self.selected_scan_name = self.scan_names_list[self.selected_scan_index]

            self.brain_vol = clIMAGEPROCESSOR.get_brain_vol(self.nifti_file_paths_list[self.selected_scan_index])
            self.selected_slice = int(self.brain_vol.shape[2]/2)
            
            self.update_texture()

    def Callback_get_next_scan(self, *_):
        if self.selected_scan_index<len(self.scan_names_list)-1: 
            self.selected_scan_index += 1 
            self.selected_scan_name = self.scan_names_list[self.selected_scan_index]

            self.brain_vol = clIMAGEPROCESSOR.get_brain_vol(self.nifti_file_paths_list[self.selected_scan_index])
            self.selected_slice = int(self.brain_vol.shape[2]/2)
            
            self.update_texture()


    def Callback_Apply_Window(self, *_):
        # text: 'Custom' # Width, Level windowing (W:70, L:30) (W:180, L:80) (W:30, L:30) (W:400, L:50) (W:2000, L:600)
        # values: 'Custom', 'Brain', 'Blood', 'Stroke', 'Soft tissue', 'Bone'
        
        
        if self.ids['id_scan_window'].text == 'Custom': return
        elif self.ids['id_scan_window'].text == 'Brain': width, level = 70,30
        elif self.ids['id_scan_window'].text == 'Blood': width, level = 180,80
        elif self.ids['id_scan_window'].text == 'Stroke': width, level = 30,30
        elif self.ids['id_scan_window'].text == 'Soft tissue': width, level = 400,50
        elif self.ids['id_scan_window'].text == 'Bone': width, level = 2000,600
        else: return
        
        self.ids['id_TextInputWindow_level'].text = f'{level}'
        self.ids['id_TextInputWindow_width'].text = f'{width}'

        self.update_texture()







    def Callback_Button_Consult(self, *_):
        self.ids['id_ProgressBarPartial'].size_hint_x = 0.96
        self.ids['id_ProgressBrowse'].bold = False
        self.ids['id_ProgressUpload'].bold = True

        self.ids['id_ScanPathInfo'].text = 'CT Scan has now been uploaded!'

        _,zip_name = os.path.split(self.selected_scan_nifti_folder)
        dest = os.path.join(self.__path_dict__['dot-cerebrum-scanner-jobs-pending'],zip_name)
        case_path = os.path.join(self.__path_dict__['dot-cerebrum-scanner-jobs-pending'],f'{zip_name}.zip')

        import json
        json_path  = os.path.join(self.selected_scan_nifti_folder, f'{zip_name}.json')
        with open(json_path, "w") as outfile: json.dump(self.patient_info, outfile)        

        import shutil
        shutil.make_archive(dest, 'zip', self.selected_scan_nifti_folder)

        import pdb; pdb.set_trace()
        
        self.upload_case_to_server(case_path=case_path)
        print('case is now uploaded to the server!')


    def upload_case_to_server(self, case_path, *_):

        clCLIENT.connect_server()
        clCLIENT.send_msg('command:receive_case')
        clCLIENT.send_file(file_path=case_path)


    ############################################
    ############################################
    ############################################


        # self.mailsentpopup = popups.AllWellPopup(id_AllWellPopupContent="[b]You successfully contacted to a neurologist.[/b]")
        # self.mailsentpopup.ids["id_AllWellOKButton"].bind(on_release=self.mailsentpopup.dismiss)
        # self.mailsentpopup.ids["id_AllWellOKButton"].bind(on_release=self.start_feedback_clock)
        # self.mailsentpopup.ids["id_AllWellOKButton"].bind(on_release=self.send_email)
        # self.mailsentpopup.open()



    ############################################
    ############################################
    ############################################








    def Callback_Button_Read_Message(self, *_):
        case_folder_path = os.path.join(self.__path_dict__['dot-cerebrum-scanner-completed'],self.patient_info['ID'])
        feedback_json_path = os.path.join(case_folder_path, 'feedback.json')

        with open(feedback_json_path, 'r') as outfile:
            feedback_json = json.load(outfile) 

        feedback = feedback_json['CS-ICH']
        
        self.FeedbackPopup = popups.FeedbackPopup(id_FeedbackPopupContent=f"[b]{feedback}[/b]")
        self.FeedbackPopup.ids["id_FeedbackOKButton"].bind(on_release=self.FeedbackPopup.dismiss)
        self.FeedbackPopup.open()


    def start_feedback_clock(self, *_):
        self.clock_feedback_check = Clock.schedule_interval(self.check_feedback_messages, 0.5)

    def check_feedback_messages(self, *_):
        case_folder_path = os.path.join(self.__path_dict__['dot-cerebrum-scanner-completed'],self.patient_info['ID'])
        feedback_json_path = os.path.join(case_folder_path, 'feedback.json')

        if os.path.exists(feedback_json_path): 
            self.number_msg = 1
            if self.ids['id_Button_Read_Message'].opacity == 1: self.ids['id_Button_Read_Message'].opacity = 0.8  
            else: self.ids['id_Button_Read_Message'].opacity = 1

        else: self.number_msg = 0
        print(self.number_msg)


    def send_email(self, *_):

        from email.message import EmailMessage
        import smtplib

        sender = "info@nekodu.com"
        recipient = "cgoksu@nekodu.com"
        message = "Case ID: {}".format(self.patient_info["ID"])

        email = EmailMessage()
        email["From"] = sender
        email["To"] = recipient
        email["Subject"] = "Acute stroke case"
        email.set_content(message)

        smtp = smtplib.SMTP("smtp.office365.com", port=587)
        smtp.starttls()
        smtp.login(sender, "QWntyZV?Wx1a8")
        smtp.sendmail(sender, recipient, email.as_string())
        smtp.quit()
