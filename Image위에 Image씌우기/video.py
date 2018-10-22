import numpy as np
import cv2

img1 = cv2.imread('logo.jpg')       # img를 읽어들임.
img2 = cv2.imread('mask.jpg')

rows, cols, channels = img1.shape
roi = img2[130:rows+130, 130:cols+130]          # 왼쪽위(0,0)에서 오른쪽으로 130만큼 이동해 원점을잡고, 그 기준으로 130 오른쪽 만큼 그림을 그림
                                                # (0,0)에서 에서 아래로 130만큼 이동해 원점을 잡고, 그 아래로 130만큼 그림 공간을 잡음.

img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img1gray, 200, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_fg = cv2.bitwise_and(img1, img1, mask = mask_inv)
img2_bg = cv2.bitwise_and(roi, roi, mask = mask)

dst = cv2.add(img1_fg, img2_bg)
img2[130:rows+130, 130:cols+130] = dst

cv2.imshow('img1gray',img1gray)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_fg',img1_fg)
cv2.imshow('img2_bg',img2_bg)
cv2.imshow('img2', img2)

cv2.waitKey(0)                  # 종료되지 않도록 키를 기다림
cv2.destroyAllWindows()






