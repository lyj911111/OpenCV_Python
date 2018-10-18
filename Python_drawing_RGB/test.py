import cv2
import numpy as np

clickflag = 0       # 클릭상태 확인 전역변수 초기값 0

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN :                         # 마우스 왼쪽버튼을 누르면
        cv2.circle(img, (x, y), 10, (255,0,0), -1)              # (x,y)마우스좌표 중심점으로 반지름 10, (B,G,R)색상, -1은 내부 모두 채움

def draw_rec(event, x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x,y), (x+100,y+100), (0,255,0), 3)  # (x,y)마우스좌표 중신점으로 100x100 사각형을 만듦

def free_drawing(event, x,y, flags, param):                     # 자유롭게 그리기
    global  clickflag                                           # 클릭상태를 확인 (전역 변수를 불러옴)

    if event == cv2.EVENT_LBUTTONDOWN:                          # 왼쪽버튼을 누르면 플레그를 1로
        clickflag = 1
    if event == cv2.EVENT_LBUTTONUP:                            # 버튼은 때면 0으로
        clickflag = 0

    if clickflag == 1:
        event = cv2.EVENT_MOUSEMOVE                             # 플레그가 1일때, 마우스가 움직여도 그림이 그려짐
        cv2.circle(img, (x, y), 10, (255, 0, 0), -1)




img = cv2.imread('./mask.jpg', cv2.IMREAD_COLOR)                                    # img에 이미지를 불러옴.
img = cv2.line(img,(0, 100), (1025, 100), (155,55,55),(30))                         # 위쪽에 가로 줄을 그음.
font = cv2.FONT_HERSHEY_DUPLEX                                                      # 텍스트의 폰트를 지정.



cv2.putText(img, "WARNNING!! This is DDOS Virus", (20, 90), font, 2,(0,0,155), 2, cv2.LINE_AA)  # 텍스트를 입력, 글자, 위치, 폰트, 크기 등


cv2.namedWindow('image')
cv2.setMouseCallback('image', free_drawing)         #  free_drawing함수 호출 (이곳에서 윈도우에서 실행결정)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 0x1B:                  # 무한 반복중, 키보드 ESC 아스키코드가 들어오면 빠져나감.
        break

cv2.destroyAllWindows()             # 창을 종료