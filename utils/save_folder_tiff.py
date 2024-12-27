import os
from PIL import Image
from tqdm import tqdm


def save_folder_as_tiff(folder_path, output_tiff_path ):
    image_file_paths = [os.path.join(folder_path ,f ) for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff'))]
    
    first_image = Image.open(image_file_paths[0])
    images = list()

    for img_path in tqdm(image_file_paths):
        img = Image.open(img_path)
        images.append(img)

    # Save all images as a multi-page TIFF
    first_image.save(output_tiff_path, save_all=True, append_images=images, compression="tiff_deflate")

