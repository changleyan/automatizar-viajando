from pyautogui import *
import pyautogui as pag
import time
import win32con
import win32api
import pygetwindow
import math

region = (1328, 0, 594, 1017)

def click(position):
    win32api.SetCursorPos(position)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def get_position(image: str, raiseException: bool = True, confidence: float = 0.8):
    try:
        position = pag.locateCenterOnScreen(image, confidence=confidence, region=region)
        # position = pag.locateCenterOnScreen(image, confidence=0.8)
        if position is None and raiseException:
            print(f'{image} not found on screen...')
            return None
        else:
            return position
    except OSError as e:
        raise Exception(e)

def checkLoading(imagen: str = "./parts/genericLoader.png"):
    print('Loading...')
    position = get_position(imagen, False)
    while position is not None:
        sleep(0.1)
        position = get_position(imagen, False)
    print('Finish Loading...')
    sleep(0.1)
    return False

def clickButton(imagen: str, confidence:float = 0.8):
    position = get_position(imagen, confidence=confidence)
    print(f'Step: {imagen}, position: {position} ....!')
    if position is not None:
        click(position)
    else:
        return False
    sleep(0.2)
    return True

def checkStay(imagen: str):
    position = get_position(imagen, False, 0.9)
    print(f'Check stay: {imagen}, position: {position} ....!')
    sleep(0.1)
    if position is None:
        return False, None
    return True, position

def slideScreen():
    print('Slide...')
    sleep(0.1)
    pag.moveTo(1610, 970, duration=0.1)
    pag.dragTo(1610, 570, button='left', duration=0.1)
    sleep(0.15)

def resizeWindow(nameWindow):
    win = pygetwindow.getWindowsWithTitle(nameWindow)[0]
    win.moveTo(1328, 0)
    win.size = (594, 1017)
    return True

def distancy_between_points(p1, p2):
    distancia = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
    return round(distancia)