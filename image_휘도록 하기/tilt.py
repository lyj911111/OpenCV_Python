import cv2
import numpy as np
from matplotlib import pyplot as plt

'''  이미지를 휘도록 하기 '''

img = cv2.imread('flippy.jpg')      #   이미지 불러오기.
rows,cols,ch = img.shape            #   이미지 가로 세로

'''  세좌표에 점찍기 '''
cv2.circle(img, (50, 50), 5, (255, 0, 0), -1)
cv2.circle(img, (200, 50), 5, (255, 0, 0), -1)
cv2.circle(img, (50, 200), 5, (255, 0, 0), -1)


pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])



M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
