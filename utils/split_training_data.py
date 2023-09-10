import csv
import os
import shutil
import numpy as np

def read_dataset_csv(csv_path):

    data_dict = dict()
    # Open the CSV file
    with open(csv_path, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        
        # Read the header row
        header = next(reader)
        
        # Print the header
        print("Header:", header)
        
        # Read and process each row of data
        for row in reader:

            id, hem_type, val = row[0].split('_')[1], row[0].split('_')[2], float(row[1])

            if f'{id}' in data_dict.keys(): pass
            else: data_dict[f'{id}'] = {}
            data_dict[f'{id}'][hem_type] = val
            valid_hem_types = ['epidural',
                            'intraparenchymal',
                            'intraventricular',
                            'subarachnoid',
                            'subdural',
                            'any',]
            if hem_type in valid_hem_types: pass
            else:
                print('Hemorrhage type error!') 
                import pdb; pdb.set_trace()

            # Process the data or perform desired operations
            # Example: Print the values of the first two columns
            print("id:", id)
            print("hem_type:", hem_type)
            print("val:", val)
            
            # Add more processing logic as needed
            
            print()  # Add a blank line between rows for clarity

        # import pdb; pdb.set_trace()
    return data_dict




def split_training_data(csv_path, png_path, dest_path):
    # csv_path = os.path.join('data','rsna-mini','stage_2_train-mini.csv') #TODO: change it
    data_dict = read_dataset_csv(csv_path)
    
    # src_path = os.path.join('data','rsna-mini','train-png') #TODO: change it
    src_path = png_path
    # dest_path = os.path.join('data','rsna-mini','train-png-splitted')

    if not os.path.exists(dest_path): os.mkdir(dest_path)

    # create train and val folders
    # trainpath = os.path.join('data','rsna-mini','train-png-splitted','train')
    # valpath = os.path.join('data','rsna-mini','train-png-splitted','val')
    trainpath = os.path.join('data','rsna','train-png-splitted','train')
    valpath = os.path.join('data','rsna','train-png-splitted','val')

    if not os.path.exists(trainpath): os.mkdir(trainpath)
    if not os.path.exists(valpath): os.mkdir(valpath)

    # create train subfolders
    dest_nohem_path = os.path.join(trainpath,'nohemorrhage')
    dest_hem_path = os.path.join(trainpath,'hemorrhage')
    if not os.path.exists(dest_nohem_path): os.mkdir(dest_nohem_path)
    if not os.path.exists(dest_hem_path): os.mkdir(dest_hem_path)
    # create val subfolders
    dest_nohem_path = os.path.join(valpath,'nohemorrhage')
    dest_hem_path = os.path.join(valpath,'hemorrhage')
    if not os.path.exists(dest_nohem_path): os.mkdir(dest_nohem_path)
    if not os.path.exists(dest_hem_path): os.mkdir(dest_hem_path)

    png_list = os.listdir(src_path)
    np.random.shuffle(png_list)


    for idx, png_name in enumerate(png_list):
        if idx<0.8*len(png_list): target_folder = 'train'
        else: target_folder = 'val'

        # dest_nohem_path = os.path.join('data','rsna-mini','train-png-splitted',target_folder,'nohemorrhage')
        # dest_hem_path = os.path.join('data','rsna-mini','train-png-splitted',target_folder,'hemorrhage')
        dest_nohem_path = os.path.join('data','rsna','train-png-splitted',target_folder,'nohemorrhage')
        dest_hem_path = os.path.join('data','rsna','train-png-splitted',target_folder,'hemorrhage')
        
        if not os.path.exists(dest_nohem_path): os.mkdir(dest_nohem_path)
        if not os.path.exists(dest_hem_path): os.mkdir(dest_hem_path)


        fpng_name = png_name.split('.')[0]
        id = fpng_name.split('_')[1]
        if id in data_dict.keys():
            if int(data_dict[id]['any']) == 0:
                # No hemorrhage detected
                shutil.copy(os.path.join(src_path,png_name), os.path.join(dest_nohem_path,png_name))
            else:
                # Hemorrhage detected
                shutil.copy(os.path.join(src_path,png_name), os.path.join(dest_hem_path,png_name))

            
            # shutil.copy(os.path.join(src_path,dcm_name), os.path.join(dest_path,dcm_name))
            # import pdb; pdb.set_trace()

    # import pdb; pdb.set_trace()




