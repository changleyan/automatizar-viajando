# from pyautogui import *
# import pyautogui as pag
# import pygetwindow
from utils import *




# pag.moveTo(1221,600, duration=0.1)
# pag.dragTo(1221,300, button='left', duration=0.1)

# data =pag.locateCenterOnScreen('./parts/omnibus/asientov.png', confidence=0.8)
# print('data:', data)

# print("position")
# position = get_position('./parts/days/27.png')
# asientoVacio = "./parts/asientos/asientov.png"
# btnSiguiente = "./parts/buttons/siguiente.png"
#
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
    # pag.moveTo(position, duration=0.2)
# pag.moveTo(position)
# pag.click()
# win = pygetwindow.getWindowsWithTitle('Nox')[0]
# win.moveTo(926, 3)
# win.size = (435, 734)
# win = pag.getWindowsWithTitle('Nox')
# print(win[0])
# resizeWindow('Nox')
# region = pag.getWindowsWithTitle('Nox')[0]
# print(region)
# region = (region.left, region.top, region.width, region.height)
# print(region)
print(pag.mouseInfo())
# print(pag.Window(hWnd=263542))
# print(pag.mouseInfo())
# a = get_position('./parts/days/27.png')
# print(a)


# day = 30
# day = "./parts/days/{}.png".format(day)
# print(day)
# l =clickButton(day, 0.99)
# print(l)
