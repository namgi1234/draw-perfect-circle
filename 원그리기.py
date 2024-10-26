import pyautogui
import time
import math

def draw_circle(radius, center_x, center_y):
    for angle in range(0, 360, 10):
        rad = math.radians(angle)
        x = center_x + radius * math.cos(rad)
        y = center_y + radius * math.sin(rad)
        if angle == 0:
            pyautogui.moveTo(x, y)
            pyautogui.mouseDown()
        else:
            pyautogui.moveTo(x, y, duration=0.001)

    pyautogui.mouseUp()


print("5초 후에 원을 그립니다. 원의 중심으로 마우스를 두세요.")
time.sleep(5)
# 마우스 위치 가져오기
center_x, center_y = pyautogui.position()
radius = 300  # 원의 반지름 설정

draw_circle(radius, center_x, center_y)

#https://neal.fun/perfect-circle/