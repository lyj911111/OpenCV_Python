import cv2
import numpy as np

cap = cv2.VideoCapture(0)       # 카메라 모듈 사용.

while(1):
    ret, frame = cap.read()     #   카메라 모듈 연속프레임 읽기

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # BGR을 HSV로 변환해줌


    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])          #  최소의 파랑색 값 범위
    upper_blue = np.array([150,255,255])        #  최대의 순수 파랑값을 지정함 (다른 값으로 변경해서 사용)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)     # 110<->150 Hue(색상) 영역을 지정.
                                                        # 50 <->255 Satuation(체도) 영역을 지정.
                                                        # 50 <->255 Value(명도) 영역을 지정.
                                                        # 영역 이하는 모두 날림 검정. 그 이상은 모두 흰색 두개로 Mask를 씌움.
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)      # 흰색 영역에 파랑색 마스크를 씌워줌.

    cv2.imshow('frame',frame)       #   원본 영상을 보여줌
    cv2.imshow('mask',mask)         #   마스크를 씌운 영상을 보여줌
    cv2.imshow('res',res)           #   마스크 위에 파랑색을 씌운 것을 보여줌.
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()







