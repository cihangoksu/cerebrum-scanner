import os
# load the data
import dicom2nifti
import dicom2nifti.settings as settings

settings.disable_validate_orthogonal()
settings.enable_resampling()
settings.set_resample_spline_interpolation_order(1)
settings.set_resample_padding(-1000)

dicom_directory = 'C:\\Users\\cgksu\\.cerebrum-scanner\\data\\CQ500-CT-0'
output_folder = 'C:\\Users\\cgksu\\.cerebrum-scanner\\data\\CQ500-CT-0-OUT'

if not os.path.exists(output_folder): os.mkdir(output_folder)
import time
now = time.time()
dicom2nifti.convert_directory(dicom_directory, output_folder)
time_elapsed = time.time() - now
print(f'Time elapsed:{time_elapsed}')