import os

from utils.config import *
from utils.save_folder_tiff import *

def convert_data_to_tiff(ouput_folder_path):
    data_folder_path = os.path.join(DATA_DIR , 'Fetus_IMG') #'isbi_dataset/data/images/'
    data_output_tiff_path = os.path.join(TIFF_DIR ,'train-volume.tif' ) #'isbi_dataset/data/train-volume.tiff'
    save_folder_as_tiff(data_folder_path, data_output_tiff_path)

    labels_folder_path = os.path.join(DATA_DIR , 'Fetus_GT') #'isbi_dataset/data/labels/'
    labels_output_tiff_path = os.path.join(TIFF_DIR ,'train-labels.tif' ) #'isbi_dataset/data/train-labels.tiff'
    save_folder_as_tiff(labels_folder_path, labels_output_tiff_path)
    # print(data_output_tiff_path , labels_output_tiff_path)

if __name__ == "__main__":
    dataset_path = os.path.join(DATA_DIR , "foetus_dataset")
    convert_data_to_tiff(dataset_path)
    


# python -m data.process_foetal_head