import cv2
import numpy as np

path = r'/mnt/D/Upwork/trials/GreenScreen.jpg'
img = cv2.imread(path)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

h_layer = hsv[:,:,0]
s_layer = hsv[:,:,1]
v_layer = hsv[:,:,2]
print(h_layer[1000,1420])
print(s_layer[1000,1420])
print(v_layer[1000,1420])

mask = np.where(((hsv[:,:,0] >= 50) &(hsv[:,:,0] <= 60) & (hsv[:,:,1] >= 195) & (hsv[:,:,2] >= 195)), 255,0)
cv2.imwrite(r'/mnt/D/Upwork/trials/GreenScreen-mask.jpg',mask)
