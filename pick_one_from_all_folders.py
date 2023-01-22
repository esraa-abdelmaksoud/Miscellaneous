import os
import random
import shutil

path = '/mnt/E/datasets/med_packs_object_annotations/'

folders = os.listdir(path)

for folder in folders:
    rn = random.randint(0,23)
    new_path = os.path.join(path,folder)
    files = os.listdir(new_path)
    cur_file = files[rn]
    shutil.copyfile(os.path.join(new_path,cur_file),os.path.join(path,cur_file))
