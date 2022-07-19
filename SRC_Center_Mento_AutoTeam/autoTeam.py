#FHD환경 
#종합정보시스템 조직관리 자동화
import pyautogui as pag
import pygetwindow as gw
import pyperclip
import pywinauto
import time
import keyboard
import threading, os
import time
from openpyxl import load_workbook
from openpyxl import Workbook

#윈도우 맨위로 가져오기
def bring_to_window() :
    win = gw.getWindowsWithTitle('종합정보시스템')[0] 
    if win.isActive == False:
        pywinauto.application.Application().connect(handle=win._hWnd).top_window().set_focus()
    win.activate() #윈도우 활성화

#항상 작동중인 스레드
class always(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self) :
        while 1:
            if keyboard.is_pressed('F4'):
                print("서브스레드,메인스레드 종료")
                pid = os.getpid()
                os.kill(pid, 2)

#always스레드
thread = always("child")
thread.daemon = True
thread.start()

num_first = 5

# bring_to_window()
check_y = 23
move_y = 0

img_first = pag.locateCenterOnScreen("./img/box_first.png",confidence=0.9)
if img_first:
    # img_first_y_next = img_first.y
    pag.click(img_first.x-15,img_first.y)
    i = 1
    while True:
        img_next = pag.locateCenterOnScreen("./img/box_next.png",confidence=0.9)
        if img_next:
            pag.click(img_next.x,img_next.y+10)
        else:
            img_next_end = pag.locateCenterOnScreen("./img/box_next_end.png",confidence=0.9)
            if img_next_end:
                pag.click(img_next_end.x,img_next_end.y+13)
                continue    
        # pag.click(img_first.x-15,img_first_y_next)
        i+=1
        if(i>=num_first):
            i=0
            # img_next = pag.locateCenterOnScreen("./img/box_next.png",confidence=0.9)
        # img_first_y_next += check_y
        # print("click:{0}".format(img_first_y_next))
 