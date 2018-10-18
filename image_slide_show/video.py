import cv2
import numpy as np


img1 = cv2.imread('flippy.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('logo.jpg', cv2.IMREAD_COLOR)
img3 = cv2.add(img1, img2)

i = 0
x = 0.1
y = 1.0
for i in range (1,100):
    x = x + 0.1
    y = y - 0.1

    img4 = cv2.addWeighted(img1, x, img2, y, 0)
    cv2.waitKey(100)
    cv2.imshow('flippy.jpg', img1)
    cv2.imshow('logo.jpg', img2)
    cv2.imshow('addtion', img3)
    cv2.imshow('Weighted addtion', img4)

    print(x,y)

cv2.waitKey(0)
cv2.destroyAllWindows()
