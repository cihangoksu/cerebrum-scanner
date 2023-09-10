import pdb
import traceback
import sys

import os
head, tail = os.path.split(os.path.join(os.path.abspath(__file__)))

import time 
from _global_paths import __path_dict__

from PIL import Image
import numpy as np

from lib import processor
clPROCESSOR = processor.Processor()

def get_ich_class(job_case_id):
    print(job_case_id)
    #### Let's do some AI shit!

    # import pdb; pdb.set_trace()
    imgpath = os.path.join(__path_dict__['dot-cerebrum-scanner-jobs'],f'{job_case_id}',f'{job_case_id}.png')
    im = Image.open(imgpath)
    im_frame = im.convert('RGB')
    np_frame = np.array(im_frame)
    img_PIL = Image.fromarray(np.uint8((np_frame - np.min(np_frame))/np.max(np_frame - np.min(np_frame))*255))
    
    hemorrhage_classification = clPROCESSOR.inference_classifier_hemorrhage(img_PIL)
    hemorrhage_class = np.argmax(hemorrhage_classification.cpu().numpy())

    ###########################
    import shutil
    src = os.path.join(__path_dict__['dot-cerebrum-scanner-jobs'],job_case_id)
    dest = os.path.join(__path_dict__['dot-cerebrum-scanner-completed'],job_case_id)
    shutil.move(src, dest)

    import json
    json_path = os.path.join(__path_dict__['dot-cerebrum-scanner-completed'],job_case_id,'cs-output.json')
    cs_output = {}
    cs_output["CS-ICH"] = int(hemorrhage_class)
    with open(json_path, "w") as out_file:
        json.dump(cs_output, out_file)

    return hemorrhage_class

def main():
    clPROCESSOR.init_classifier_ich()
    print('ICH classifier has been initialized.')

    while True:
        time.sleep(0.5)
        jobs_list = sorted(os.listdir(__path_dict__['dot-cerebrum-scanner-jobs']))

        if len(jobs_list)>0: 
            firstjob = jobs_list[0]
            hem_class = get_ich_class(firstjob)
            hem_feedback = 'Hemorrhage suspected!' if hem_class == 0 else 'No hemorrhage suspected.'
            print(hem_class)
            print(hem_feedback)




if __name__ == '__main__':
    main()