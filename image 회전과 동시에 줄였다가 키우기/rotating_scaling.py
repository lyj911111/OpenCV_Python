import cv2
import numpy as np

img = cv2.imread('mask.jpg', 0)     #   사용할 이미지 파일 흑백(0)
rows, cols = img.shape

flag = 0        #   스케일을 줄이고 키우기 위한 플레그

scale = 1       #   초기값설정
angle = 0

while True:
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, scale)     #
    dst = cv2.warpAffine(img, M, (cols, rows))

    angle = angle + 10      #   각을 10도 씩 회전
    if angle == 360:        #   0도~360도
        angle = 0

    if flag == 0:               #   스케일이 점점 줄어듦
        scale = scale - 0.01
        if scale <= 0:
            flag = 1

    if flag == 1:               #   스케일이 점점 늘어남
        scale = scale + 0.01
        if scale >= 1:
            flag = 0


    cv2.imshow('img', dst)      #   이미지 출력
    if cv2.waitKey(50) == 27:   #   esc 누르면 종료
        break



cv2.destroyAllWindows()
