import numpy as np
import cv2

img = cv2.imread('ci.png')                                              # 이미지 불러오기
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                          #   BGR -> Gray로
ret, thresh = cv2.threshold(imgray, 200, 255, cv2.THRESH_BINARY_INV)    #   이진으로 분리하여 흑과 백으로.

# 이미지에서  contour 를 탐색
image1, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)    # 컨투어를 찾아냄.

#탐색된 contour 를 원본에 넣음.
cv2.drawContours(img, contours, -1, (0,0,255), 1)  # 빨간색으로 전체 컨투어를 그림

cv2.imshow('origin', img)
cv2.imshow('gray', imgray)
cv2.imshow('threshold', thresh)
cv2.imshow('contour', image1)

cv2.waitKey(0)
cv2.destroyAllWindows()
