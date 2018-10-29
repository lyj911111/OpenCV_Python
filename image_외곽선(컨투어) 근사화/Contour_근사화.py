# 블록성 결함. (Convexity Defects) : Contour 라인에서 블록체가 되지 못하게 오목하게 들어간 부분.

import cv2
import numpy as np

img = cv2.imread('star.jpg')                                # 이미지 불러오기
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)              # 이미지 그레이 전환

ret, thresh = cv2.threshold(imgray, 120, 255, 0)                                                # 흑과 백으로
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   # contour를 찾아냄.(좌표)

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)     #   contour 외곽선을 그림, 초록색 두께2로...
cnt = contours[0]                                       #   cnt 에 Contour[0] 의 2차원 좌표를 넣음.



hull = cv2.convexHull(cnt, returnPoints=False)  #   False로 하면 그릴때 썼던 좌표가 아니고, **인덱스만 얻음. (Convex한 모양을 같느냐, 벗어났느냐)

defects = cv2.convexityDefects(cnt, hull)   #

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]          # s : start점과 end점 far 거리가 얼마나 되는가 오목한 점.
    start = tuple(cnt[s][0])            # 반환된 s인덱스
    end = tuple(cnt[e][0])              # 반환된 e인덱스
    far = tuple(cnt[f][0])              # 반환된 f인덱스
    cv2.line(img, start, end, [255, 0, 0], 2)
    cv2.circle(img, far, 5, [0, 0, 255], -1)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()




