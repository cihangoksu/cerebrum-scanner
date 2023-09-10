# processor-class
from __future__ import print_function, division

import sys
import os
head, tail = os.path.split(os.path.join(os.path.abspath(__file__)))

import os
# load the data
import dicom2nifti
import dicom2nifti.settings as settings

import time 

class ImageProcessor(object):
    def __init__(self):
        super(ImageProcessor, self).__init__()

        # self.dicom_directory = 'C:\\Users\\cgksu\\.cerebrum-scanner\\data\\CQ500-CT-0'
        # self.output_folder = 'C:\\Users\\cgksu\\.cerebrum-scanner\\data\\CQ500-CT-0-OUT'

        self.dicom_directory = None
        self.output_folder = None

        self.brain_vol_dict = {}
        # brain_vol = nib.load('C:\\Users\\cgksu\\.cerebrum-scanner\\data\\CQ500-CT-0-OUT\\2_plain.nii.gz')

    def convert_dicom_folder_to_nifti(self,*_):
        settings.disable_validate_orthogonal()
        settings.enable_resampling()
        settings.set_resample_spline_interpolation_order(1)
        settings.set_resample_padding(-1000)

        if not os.path.exists(self.output_folder): os.mkdir(self.output_folder)
    
        now = time.time()
        dicom2nifti.convert_directory(self.dicom_directory, self.output_folder)
        time_elapsed = time.time() - now
        print(f'Time elapsed:{time_elapsed}')


    def get_brain_vol_dict(self, nifti_folder_path, *_):

        for path in nifti_folder_path:
            brain_vol = self.get_brain_vol(path)
            _, tail = os.path.split(path)
            self.brain_vol_dict[tail] = brain_vol




    def get_brain_vol(self, nifti_path_brain_vol, *_):

        import nibabel as nib
        brain_vol = nib.load(nifti_path_brain_vol)
        brain_vol_data = brain_vol.get_fdata()

        return brain_vol_data












