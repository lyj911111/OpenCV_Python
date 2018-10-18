import numpy as np
import cv2

img1 = cv2.imread('flippy.jpg', cv2.IMREAD_COLOR)       # img를 읽어들임.
img2 = cv2.imread('logo.jpg', cv2.IMREAD_COLOR)


fourcc = cv2.VideoWriter_fourcc(*'XVID')                        # 내가 사용할 코덱
out = cv2.VideoWriter('output.avi', fourcc, 5.0, (400, 400))   #  코덱 / 1초에 x개의 프레임이 실행 / 400x400 크기를 맞춤.

x = 0.1
y = 1.0

for i in range (0,100):
    x = x + 0.1                                     # x는 0.1 -> 1.0으로,  y는 1.0에서 -> 0.1으로
    y = y - 0.1
    img3 = cv2.addWeighted(img1, x, img2, y, 0)     # img3에 x,y의 변화를 줌. (점점 픽셀값을 합침)
    out.write(img3)                                 # img3를 동영상으로 출력(저장)
    cv2.imshow('frame',img3)                        # 코드 실행시 실행시킬시 바로 출력.
    cv2.waitKey(100)                                # 천천히 볼수 있도록.



    if cv2.waitKey(1) & 0xFF == ord('q'):           # q를 누르면 종료
        break


out.release()
cv2.destroyAllWindows()





