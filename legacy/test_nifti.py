import matplotlib.pyplot as plt

import nibabel as nib
brain_vol = nib.load('C:\\Users\\cgksu\\.cerebrum-scanner\\data\\CQ500-CT-0-OUT\\2_plain.nii.gz')
type(brain_vol)

brain_vol_data = brain_vol.get_fdata()
type(brain_vol_data)

brain_vol_data.shape

plt.imshow(brain_vol_data[96], cmap='bone')
plt.axis('off')
plt.show()

import pdb; pdb.set_trace()