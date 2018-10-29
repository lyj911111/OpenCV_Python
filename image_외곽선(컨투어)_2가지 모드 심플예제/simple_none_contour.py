import numpy as np
import cv2

img = np.zeros((300, 400, 3), np.uint8)                                 # 300x400 의 칼라영역을 생성.

img1 = cv2.rectangle(img, (50, 100), (350, 200), (255, 255, 255), -1)   # 칼라의 직사각형 생성.
img2 = img1.copy()                                                      # 이미지 복사

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                          # 이미지를 그레이로.

# Chain approx none 로 근사법으로  contour 를 찾음.
image1, contours1, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Chain approx simple 로 근사법으로  contour 를 찾음.
image2, contours2, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print('APPROX_NONE : ', contours1[0].shape)     # 800개의 포인트가 찍힘.  / contour1[0] 안에 2차원의 배열값[] [] 이 들어있다. 즉 이미지의 윤곽정보가 contour1[0] 안에 들어있다.
print('APPROX_SIMPLE : ', contours2[0].shape)   # simple로 하면, 꼭지점부분만. / / contour2[0] 안에 2차원의 배열값[] [] 이 들어있다.

# 이미지에  contour 그리기
for i in contours1[0]:
    cv2.circle(img1, (i[0][0], i[0][1]), 3, (0, 0, 255), -1)

for i in contours2[0]:
    cv2.circle(img2, (i[0][0], i[0][1]), 3, (0, 0, 255), -1)


cv2.imshow('APPROX_NONE', img1)
cv2.imshow('APPROX_SIMPLE', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
