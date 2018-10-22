import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('timetable.png', 0)     #  0으로 읽는다: Gray Scale로 만들겠다. ( Gray Scale로만 됨)
img = cv2.medianBlur(img, 5)             #   영상의 고주파(튀는부분)을 평활화 해줌.

ret,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)                                      #   전통적인 Threahold방식 (1과 0으로 나눔)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)     #   평균 부분의 필터 (가로11, 세로11) 에 대한 픽셀 필터 / 영상의 불필요한 부분을 날리고 필요한 선만 찾음.
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2) #   가우시안(가운데 비율이 높아지는) 부분의 필터

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i],'gray')        #   처리한 원본(gray로 변환한)과 사진을 출력
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
