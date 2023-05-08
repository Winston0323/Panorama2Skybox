from PIL import Image
from scipy.ndimage import map_coordinates
import numpy as np
import glob
import cv2
import py360convert
import os
image_path = glob.glob("Input/*.jpg")
image_list = []

# read all images
folder_name = "Result"
os.mkdir(folder_name)
index = 1
for path in image_path:
    
    image_name = path[6:-4]
    # Open the panorama image
    panorama_image = cv2.imread(path)
    # Convert the panorama to a cubemap
    cubemap = py360convert.e2c(panorama_image, face_w=512, cube_format='list')
    
    
    new_folder_path = os.path.join(folder_name, image_name)
    os.mkdir(new_folder_path)

    cv2.imwrite(f'{new_folder_path}/nz.jpg', cubemap[0])
    cv2.imwrite(f'{new_folder_path}/nx.jpg', cv2.flip(cubemap[1], 1))
    cv2.imwrite(f'{new_folder_path}/pz.jpg', cv2.flip(cubemap[2], 1))
    cv2.imwrite(f'{new_folder_path}/px.jpg', cubemap[3])
    cv2.imwrite(f'{new_folder_path}/py.jpg', cv2.flip(cubemap[4], 1))
    cubemap[5] = cv2.rotate(cubemap[5], cv2.ROTATE_90_CLOCKWISE)
    cubemap[5] = cv2.rotate(cubemap[5], cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(f'{new_folder_path}/ny.jpg', cubemap[5])    
    index+=1