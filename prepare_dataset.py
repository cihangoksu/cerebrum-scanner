#%%
from utils import prepare_data, split_training_data
import os
def convert_dicom_to_png(dicom_folder_path,png_path):
   print('Lets check prepare_data')
   
   
   for dicom_file_name in sorted(os.listdir(dicom_folder_path)):
      dicom_path = os.path.join(dicom_folder_path, dicom_file_name)
      prepare_data.prepare_and_save(dicom_path, png_path)
   


def main():
   home_folder = os.path.expanduser("~")
   rsna_folder_path = os.path.join(home_folder,'Downloads', 'rsna-intracranial-hemorrhage-detection','rsna-intracranial-hemorrhage-detection')
   # dicom_folder_path = os.path.join(os.getcwd(), 'data', 'rsna-mini','train')
   dicom_folder_path = os.path.join(rsna_folder_path,'stage_2_train')
   if not os.path.exists(os.path.join(os.getcwd(), 'data', 'rsna')): os.mkdir(os.path.join(os.getcwd(), 'data', 'rsna'))
   # png_folder_path = os.path.join(os.getcwd(), 'data', 'rsna-mini','train-png')
   png_folder_path = os.path.join(os.getcwd(), 'data', 'rsna','train-png')

   print('now we start')
   convert_dicom_to_png(dicom_folder_path=dicom_folder_path, png_path=png_folder_path)

   # csv_path = os.path.join(os.getcwd(), 'data', 'rsna-mini','stage_2_train-mini.csv')
   csv_path = os.path.join(rsna_folder_path,'stage_2_train.csv')
   
   # dest_path = os.path.join(os.getcwd(), 'data', 'rsna-mini','train-png-splitted')
   dest_path = os.path.join(os.getcwd(), 'data', 'rsna','train-png-splitted')

   split_training_data.split_training_data(csv_path, png_folder_path, dest_path)
   
   return None


#%%
# Main function executor
if __name__ == "__main__":
   main()