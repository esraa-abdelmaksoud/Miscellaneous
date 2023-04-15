
import os
import warnings
import sys
import time

import pytesseract
import fitz
from PIL import Image
import csv
import shutil
import click
from datetime import datetime

file_path = r'/mnt/D/Upwork/Fatima-UAE/E__kunden_homepages_46_d953515319_www_uploaddocuments_lib12__MX-M265N_20230328_115200.pdf'

doc = fitz.open(file_path)

for p in range(len(doc)):
    page = doc.load_page(p)
    pix = page.get_pixmap(dpi=200)
    s = datetime.now()
    # img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    pix.save(f'/mnt/D/Upwork/Fatima-UAE/temp_output/{p}.png')
    # print(img)
    img = Image.open(f'/mnt/D/Upwork/Fatima-UAE/temp_output/{p}.png')
    tess_txt = pytesseract.image_to_string(img, lang="eng+ara")
    os.remove(f'/mnt/D/Upwork/Fatima-UAE/temp_output/{p}.png')
    # print(tess_txt)
    print(datetime.now()-s)
