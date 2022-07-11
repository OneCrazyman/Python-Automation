#버튼클릭 (locate이미지)
import random, keyboard, os, mouse
import time
import pyautogui as pag
import pyperclip

# img_maeu = pag.locateCenterOnScreen("maeu.png")
# pag.click(img_maeu)
first_page = True
while True:
    if keyboard.is_pressed('F4'):
        print("서브스레드,메인스레드 종료")
        pid = os.getpid()
        os.kill(pid, 1)

    if(first_page):
        img_maeu = pag.locateCenterOnScreen("maeu.png",confidence=0.9)
        pag.click(img_maeu)
        time.sleep(0.01)
        img_num_one = pag.locateCenterOnScreen("num_one.png",confidence=0.9)
        print(img_num_one)
        # btn_click(img_num_one,0,0,0,0)
        if img_num_one:
            pag.moveTo(img_num_one.x,img_num_one.y+10,duration=0.1)
            pag.click()
            time.sleep(0.4)

    # mouse.move(0,-20)
    # mouse.click()
    img_hangmok = pag.locateCenterOnScreen("hangmok.png",confidence=0.99)
    if img_hangmok:

        img_maeu = pag.locateCenterOnScreen("maeu.png",confidence=0.9)
        pag.click(img_maeu)

        first_page=False
        img_scroll = pag.locateCenterOnScreen("scroll.png",confidence=0.8)
        if img_scroll:
            pag.moveTo(img_scroll.x,img_scroll.y,duration=0.0)
            pag.scroll(-10)
        img_jg = pag.locateCenterOnScreen("jg.png",confidence=0.8)
        if img_jg:
            pag.click(img_jg)
            pag.click(img_jg.x+300,img_jg.y)
            time.sleep(1)
            pyperclip.copy("감사합니다.")
            pag.hotkey("ctrl","v")
            
            img_svae =pag.locateCenterOnScreen("svae.png",confidence=0.8)
            if(img_svae):
                pag.click(img_svae)
            img_check=pag.locateCenterOnScreen("check.png",confidence=0.8)
            if img_check:
                pag.click(img_check)
                time.sleep(0.3)
            img_check=pag.locateCenterOnScreen("check.png",confidence=0.8)
            if img_check:
                pag.click(img_check)
                time.sleep(0.3)
                first_page=True
                

    # time.sleep(0.5)