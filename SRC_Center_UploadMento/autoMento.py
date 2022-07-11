import pyautogui as pag
import pygetwindow as gw
import pywinauto
# import mss, cv2
# import numpy as np
import random, time
import keyboard
import threading, os

def bring_to_window() :
    win = gw.getWindowsWithTitle('종합정보시스템')[0] 
    if win.isActive == False:
        pywinauto.application.Application().connect(handle=win._hWnd).top_window().set_focus()
    win.activate() #윈도우 활성화

def push_btn(typing):
    time.sleep(random.uniform(0.10,0.1456))
    pag.keyDown(typing)
    time.sleep(random.uniform(0.256,0.356))
    pag.keyUp(typing)

# bring_to_window()
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

while True:
    load_count = 0

    img_add = pag.locateCenterOnScreen("./img/add.png",confidence=0.9)
    if(img_add):
        print("추가..")
        pag.click(img_add.x,img_add.y-13)
        time.sleep(0.5)
        while True:
            print("로딩중..")
            if (load_count<2):
                img_name = pag.locateCenterOnScreen("./img/name.png",confidence=0.9)
                load_count+=1
            img_loading = pag.locateCenterOnScreen("./img/loading.png",confidence=0.9)
            if(not img_loading):
                break
        print("로딩완료..")
        print("학생조회")
        if(img_name):
            pag.click(img_name.x+50,img_name.y)
            print("입력필요")
            while True:
                if(keyboard.is_pressed("space")):
                    break
            print("입력완료")
            img_check = pag.locateCenterOnScreen("./img/check.png",confidence=0.9)
            if (img_check):
                pag.click(img_check)
                time.sleep(0.3)
                print("등록완료")
                img_team = pag.locateCenterOnScreen("./img/team.png",confidence=0.9)
                if (img_team):
                    pag.click(img_team.x-10,img_team.y)
                    print("팀입력")
                    while True:
                        if keyboard.is_pressed("1"):
                            break
                        elif keyboard.is_pressed("2"):
                            break
                        elif keyboard.is_pressed("3"):
                            break
                        elif keyboard.is_pressed("4"):
                            break