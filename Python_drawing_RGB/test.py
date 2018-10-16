import cv2
import numpy as np

clickflag = 0

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(img, (x, y), 10, (255,0,0), -1)              # (x,y)마우스좌표 중심점으로 반지름 10, (B,G,R)색상, -1은 내부 모두 채움

def draw_rec(event, x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x,y), (x+100,y+100), (0,255,0), 3)

def free_drawing(event, x,y, flags, param):
    global  clickflag

    if event == cv2.EVENT_LBUTTONDOWN:
        clickflag = 1
    if event == cv2.EVENT_LBUTTONUP:
        clickflag = 0

    if clickflag == 1:
        event = cv2.EVENT_MOUSEMOVE
        cv2.circle(img, (x, y), 10, (255, 0, 0), -1)




img = cv2.imread('./mask.jpg', cv2.IMREAD_COLOR)                                    # img에 이미지를 불러옴.
img = cv2.line(img,(0, 100), (1025, 100), (155,55,55),(30))                         # 위쪽에 가로 줄을 그음.
font = cv2.FONT_HERSHEY_DUPLEX                                                      # 텍스트의 폰트를 지정.
is_mouse_pressing = False          # 마우스가 눌렸는가 확인


cv2.putText(img, "WARNNING!! This is DDOS Virus", (20, 90), font, 2,(0,0,155), 2, cv2.LINE_AA)  # 텍스트를 입력, 글자, 위치, 폰트, 크기 등


cv2.namedWindow('image')
cv2.setMouseCallback('image', free_drawing)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 0x1B:                  # 무한 반복중, 키보드 ESC 아스키코드가 들어오면 빠져나감.
        break

cv2.destroyAllWindows()