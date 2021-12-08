import os
from PIL import Image
import cv2


txt_dir = 'C://Users//Administrator//Desktop//123//JSON//txt'
img_dir = 'C://Users//Administrator//Desktop//123//JPG'
file_name = 'AM_sunny_CI04_20211101_100709_1393_3.'
img = cv2.imread(os.path.join(img_dir, file_name + 'jpg'))

with open(os.path.join(txt_dir, file_name + 'txt'), 'r') as f:
    a = f.readline()
s, x, y, w, h = a.rstrip('\n').split(' ')
x = float(x)
y = float(y)
w = float(w)
h = float(h)

cv2.rectangle(img, (round(x), round(y)), (round(x+w), round(y+h)),(255, 0, 0), 3)
# cv2.rectangle(img, (round(x-(w/2)), round(y-(h/2))), (round(x+(w/2)), round(y+(h/2))), (255, 0, 0), 3)
cv2.imshow('img', img)
cv2.waitKey()