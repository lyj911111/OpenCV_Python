import cv2
import numpy as np

img = cv2.imread('hand.png')                        #   이미지 불러오기
img1 = img.copy()                                   #   이미지를  img1에 복사.
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)      #   이미지를  gray로 변환.
ret, thresh = cv2.threshold(imgray, 120, 255, 0)    #   변환된 이미지에 threshold를 적용, 흑과 백으로.


image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]                                     # cnt에 contour[0] 에 있는 외곽선의 좌표값을 갖도록 함.
cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)       # 그 좌표값을 읽고 외곽선을 그림.
cv2.imshow('Original contour', img)                   # Contour가 적용된 이미지를 보여줌.

##################### contour -> convex   #########################

chk = cv2.isContourConvex(cnt)                  #   Contour 가 Convex인지 확인함.

if not chk:
    cvxhull = cv2.convexHull(cnt)                           #   convex 의 좌표를 2차원으로 찾아줌.
    cv2.drawContours(img1, [cvxhull], 0, (0, 255, 0), 3)    #   찾은 좌표를 그려줌.
    cv2.imshow('ConvexHull', img1)                          #   그 이미지를 보여줌.


cv2.waitKey(0)
cv2.destroyAllWindows()