import cv2
import numpy as np

img = cv2.imread('mask.jpg')        #   내가 쓸 이미지 정함.

#res = cv2.resize(img,None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

height, width = img.shape[:2]   # 높이와 폭을 받음.

res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)      #   사진의 사이즈를 조정함. (가로,세로 2배를 늘림.)

cv2.imshow('origin', img)       #   원본 영상.
cv2.imshow('resizing', res)     #   사이즈 업

cv2.waitKey(0)
cv2.destroyAllWindows()
