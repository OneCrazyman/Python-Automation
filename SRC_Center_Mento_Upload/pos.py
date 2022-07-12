from ctypes.wintypes import POINT
import pyautogui as pag
import pygetwindow as gw
import time, keyboard, mouse
import pywinauto
import threading,os


def bring_to_window() :
    win = gw.getWindowsWithTitle('던전앤파이터 모바일')[0] 
    if win.isActive == False:
        pywinauto.application.Application().connect(handle=win._hWnd).top_window().set_focus()
    win.activate() #윈도우 활성화

# bring_to_window()

while 1:
    if keyboard.is_pressed('F4'):
        print("end")
        pid = os.getpid()
        os.kill(pid, 1)
    if keyboard.is_pressed('F2'):
        # pag.click(177,51)
        x, y = pag.position()
        time.sleep(0.1)
        print("%s,%s" % (x,y))