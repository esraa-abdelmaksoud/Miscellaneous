import pytesseract
from pytesseract import Output
import cv2
import os
import pandas as pd
import shutil
# Setting configration
folder_path ='/mnt/D/images/'
config='--psm 3'


def draw_boxes(folder_path: str) -> str:
    boxes_dir = os.path.join(folder_path,"ocr_boxes")
    if os.path.isdir(boxes_dir):
        shutil.rmtree(boxes_dir)
    os.mkdir(boxes_dir)
    files = os.listdir(folder_path)
    files.remove("ocr_boxes")
    for f in range(len(files)):
        cur_file = os.path.join(folder_path,files[f])
        img = cv2.imread(cur_file)

        df = pytesseract.image_to_data(img, lang='rus',output_type=Output.DICT,config='{}'.format(config))
        boxes = len(df['level'])

        for i in range(boxes):
            if len(df['text'][i]) > 0:
                (x, y, w, h) = (df['left'][i], df['top'][i], df['width'][i], df['height'][i])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)
        output_path = os.path.join(folder_path,"ocr_boxes", files[f])
        new_df = pd.DataFrame.from_dict(df)
        new_df.to_csv(f"{output_path[:-4]}.csv")
        cv2.imwrite(output_path,img)
    return "Boxes were successfully drawn!"


draw_boxes(folder_path)
