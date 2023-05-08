import glob
import os

image_path = glob.glob("Input/*.jpg")
image_list = []
index = 1
for path in image_path:
    print(path)
    os.rename(path,"Input/"+str(index) + ".jpg")
    index+=1
image_path = glob.glob("Input/*.jpg")