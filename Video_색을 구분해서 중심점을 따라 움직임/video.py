import cv2
import numpy as np

cap = cv2.VideoCapture(0)   #  비디오 영상을 캡쳐하기로함.

while True:
    ret, frame = cap.read()     #   영상 연속으로 읽기.

    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)              #  필터
    gray = cv2.cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                      #   원본을 gray로 전환, gray 로 영상 읽을때 사용. ex)  => cv2.imshow('frame', gray)
    ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)      #   gray 값을 흑과 백으로 이진화 시킴. (Threshold 시키기.) 이진화 시킨 값은 thresh에 저장됨.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # BGR -> HSV로 변환.


    lower_blue = np.array([100,50,50])          # 파랑색 범위
    upper_blue = np.array([150,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)     # 110<->150 Hue(색상) 영역을 지정.
                                                        # 영역 이하는 모두 날림 검정. 그 이상은 모두 흰색 두개로 Mask를 씌움.
    res = cv2.bitwise_and(frame, frame, mask=mask)      # 흰색 영역에 파랑색 마스크를 씌워줌.

    ret, thresh = cv2.threshold(mask, 150, 255, cv2.THRESH_BINARY_INV)      #   배경이 흰색
    ret, thresh = cv2.threshold(thresh, 150, 255, cv2.THRESH_BINARY_INV)    #   배경이 검정색이 나오도록 2번 해줌.


    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #   이진화된 값을 이용해 외곽선을 찾아냄. 그리고 contours에 값이 저장됨.
    cv2.drawContours(res, contours, -1, (0, 255, 0), 2)  # ( 첫번째 인자 )에 컨투어(외곽선)을 그려줌.


    mom = contours[0]
    M = cv2.moments(mom)
    area = cv2.contourArea(mom)
    print(area)

    cv2.imshow('b_frame', blurred_frame)
    cv2.imshow('frame', frame)          # 원본 영상을 보여줌
    cv2.imshow('thresh', thresh)        # 이진화된 영상을 보여줌
    cv2.imshow('image', image)      # 빨강색에 외곽선 씌우기.
    cv2.imshow('res', res)



    if cv2.waitKey(1) & 0xFF == ord('q'):                   #  'q'를 누르면 종료.
        break

cap.release()
cv2.destroyAllWindows()