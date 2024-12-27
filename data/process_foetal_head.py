import os
from PIL import Image
import numpy as np
import random
import cv2

from utils.config import *
from utils.save_folder_tiff import *
from utils.constants import *

def construct_data_splits(imgs_path, labels_path):
    imgs = Image.open(imgs_path)
    labels = Image.open(labels_path)

    data = list()

    for n in range(imgs.n_frames):
        imgs.seek(n)
        labels.seek(n)

        train_img = np.asarray(imgs)
        train_label = np.asarray(labels)
        data.append((train_img, train_label))

    random.shuffle(data)
    print(len(data))
    
    if (TRAIN_SIZE + VAL_SIZE + TEST_SIZE) == 100 :

        train_data_size = int(TRAIN_SIZE/100 * len(data))
        val_data_size = int(VAL_SIZE/100 * len(data))

        train_list = data[ : train_data_size ]
        val_list = data[ train_data_size : train_data_size + val_data_size ]
        test_list = data[ train_data_size + val_data_size : ]

        save_splitted_files(train_list, TRAIN_IMGS_DIR, TRAIN_LABELS_DIR)
        save_splitted_files(val_list, VAL_IMGS_DIR, VAL_LABELS_DIR)
        save_splitted_files(test_list, TEST_IMGS_DIR, TEST_LABELS_DIR)
    else:
        raise Exception("Split percentages do not account for the entire dataset.")

def save_splitted_files(data_list, imgs_dir, labels_dir):
    for idx, data in tqdm(enumerate(data_list, 1)):
        img, label = data
        img_dst = os.path.join(imgs_dir, f'{idx:02}.png')
        label_dst = os.path.join(labels_dir, f'{idx:02}.png')
        cv2.imwrite(img_dst, img)
        cv2.imwrite(label_dst, label)

if __name__ == "__main__":
    data_folder_path = os.path.join(DATA_DIR , 'Fetus_IMG') #'isbi_dataset/data/images/'
    data_output_tiff_path = os.path.join(TIFF_DIR ,'train-volume.tif' ) #'isbi_dataset/data/train-volume.tiff'
    save_folder_as_tiff(data_folder_path, data_output_tiff_path)

    labels_folder_path = os.path.join(DATA_DIR , 'Fetus_GT') #'isbi_dataset/data/labels/'
    labels_output_tiff_path = os.path.join(TIFF_DIR ,'train-labels.tif' ) #'isbi_dataset/data/train-labels.tiff'
    save_folder_as_tiff(labels_folder_path, labels_output_tiff_path)

    construct_data_splits(data_output_tiff_path , labels_output_tiff_path)
    


# python -m data.process_foetal_head