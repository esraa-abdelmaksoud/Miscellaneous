import pytesseract
from pytesseract import Output
import cv2
# Setting configration
imageName='i (62)'
config='--psm 6'

# Readibg image
image = cv2.imread(r'D:\Practical\ocrtestimages\{} resized {}.jpg'.format(imageName))

# Creating OCR data frame
df = pytesseract.image_to_data(image, output_type=Output.DICT,config='{}'.format(config))
n_boxes = len(df['level'])

# Drawing rectangles around recognized text
for i in range(n_boxes):
    (x, y, w, h) = (df['left'][i], df['top'][i], df['width'][i], df['height'][i])
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Showing image
cv2.imshow('img', image)
cv2.waitKey(0)

# Writing image to disk
cv2.imwrite(r'D:\Practical\ocrtestimages\{} resized {} boxes {}.jpg'.format(imageName,config), image)