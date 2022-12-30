import os
import random
import shutil

path = "/mnt/E/datasets/med_packs"

# Create train and test folders
try:
    os.mkdir(f"{path}/train")
    os.mkdir(f"{path}/test")
except:
    pass

# Get pharma folders
folders_list = os.listdir(path)

# Create pharma folders in test folders
try:
    for folder in folders_list:
        os.mkdir(f"{path}/test/{folder}")
except:
    pass

# Pick arbitrary files and move files
for folder in folders_list:
    if folder not in ['train', 'test']:
        files = os.listdir(f"{path}/{folder}")

        file_1 = files[random.randint(0,25)]
        files.remove(file_1)
        file_2 = files[random.randint(0,24)]

        shutil.move(f"{path}/{folder}/{file_1}",f"{path}/test/{folder}/{file_1}")
        shutil.move(f"{path}/{folder}/{file_2}",f"{path}/test/{folder}/{file_2}")
        
        # Move the rest to train
        shutil.move(f"{path}/{folder}",f"{path}/train")
