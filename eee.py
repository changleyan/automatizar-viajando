# from pyautogui import *
# import pyautogui as pag
# import pygetwindow
from utils import *
from datetime import datetime
from playsound import playsound
from pathlib import Path



# pag.moveTo(1221,600, duration=0.1)
# pag.dragTo(1221,300, button='left', duration=0.1)

# data =pag.locateCenterOnScreen('./assets/asientoVacio.png', confidence=0.8)
# print('data:', data)

# print("position")
# position = get_position('./assets/days/27.png')
# asientoVacio = "./assets/asientoVacio.png"
# # btnSiguiente = "./assets/siguiente.png"
# #
# vacios = list(locateAllOnScreen(asientoVacio, region=region, confidence=0.9))
#
# print(vacios)
#
# for i in range(4):
#     position = center(vacios[i])
#     print(position)
#     click(position)
#     sleep(0.1)
#     checkLoading()
#
# timer = 0
# while True:
#     print("Waiting for" + str(0))
#     timer += 1;
#     sleep(2)
#     data =pag.locateCenterOnScreen('./assets/load.png', confidence=0.8)
#     print('data:', data)
    # pag.moveTo(position, duration=0.2)
# pag.moveTo(position)
# pag.click()

# win = pygetwindow.getWindowsWithTitle('LDPlayer')[0]
# resizeWindow('LDPlayer')



import win32gui
#current = win32gui.GetWindowText('MEmu')
# hwnd = win32gui.FindWindow(None, 'MEmu')
#hwnd = win32gui.FindWindowEx(hwnd, 0, 'MEmu', None)
# print(hwnd)
# win32gui.MoveWindow(hwnd, 0, 0, 1000, 700, True)
# win.size = (435, 734)
# win = pag.getWindowsWithTitle('Nox')
# print(win)
# resizeWindow('MEMU')
# region = pag.getWindowsWithTitle('Nox')[0]
# print(region)
# region = (region.left, region.top, region.width, region.height)
# print(region)
# pag.moveTo(1610, 670, duration=0.1)
# pag.dragTo(1610, 500, button='left', duration=0.5)
# sleep(0.15)
print(pag.mouseInfo())
# notification_route = "{}/assets/notificacion.wav".format(Path().absolute())
# notification_route = notification_route.replace('\'' , "/")
# print(notification_route)
# # playsound()
# playsound("C:/Users/CHANG/WORK/viajando/automatizar-viajando/assets/notificacion.wav")
# dt = datetime.now()
# ts = datetime.timestamp(dt)
# ruta = "C:/Users/CHANG/Pictures/Pasajes/{}.png".format(ts)
# pag.screenshot(ruta, region=region)
# print(pag.Window(hWnd=263542))
# print(pag.mouseInfo())
# a = get_position('./assets/days/27.png')
# print(a)


# day = 30
# day = "./assets/days/{}.png".format(day)
# print(day)
# l =clickButton(day, 0.99)
# print(l)
