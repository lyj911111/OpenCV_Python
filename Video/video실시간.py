import numpy as np
import cv2

cap = cv2.VideoCapture(0)       # 기본이 0번, 만약 비디오가 2개이면 1번 cap이라는 변수에 넣어서 핸들링함.

while(True):
    ret, frame = cap.read()     # 정상적인 값을 받으면, ret가 True이고, cap.read하면 한 프레임씩 읽어들임.

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                       #GRAY하면 흑백으로 나옴
    cv2.imshow('frame', frame)           #   한장을 받아서 계속적으로 한장씩 출력하는 것임.

    if cv2.waitKey(1) & 0xFF == ord('q'):   #   q가 나오면 종료
        break

cap.release()
cv2.destroyAllWindows()