from utils import waitForLoadingOver, checkImageneOnScreen, pag, region, click, findImageAndClick, with_screen
from datetime import datetime
from pyautogui import sleep

def click_to_omnibus(capture: bool, position):
    if capture:
        ruta = f"C:/Users/CHANG/Pictures/Pasajes/{datetime.now().timestamp()}.png"
        pag.screenshot(ruta, region=region)

    sleep(0.2)
    click(position)
    sleep(0.2)
    waitForLoadingOver()
    sleep(0.2)
    return True, False

def select_viaje(capture: bool, exactDay: bool, checkTrain: bool):
    btnBuscar = f"./assets/{with_screen()}/btnBuscar.png"        # Botón de buscar
    exactDayFail = f"./assets/{with_screen()}/exactDayFail.png"  # Mensaje que sale cuando no hay pasajes para ese día
    existCapacity = f"./assets/{with_screen()}/btnOmnibus.png"   # Mensaje que sale cuando  hay pasajes aunque no sea del día
    trainMenu = f"./assets/{with_screen()}/btnTren.png"          # Botón del menú de tren

    if findImageAndClick(btnBuscar):
        waitForLoadingOver()

        # Verificar que existan pasajes de algún día
        is_capacity, position = checkImageneOnScreen(existCapacity)
        if exactDay:
            # Verificar si no hay en omnibus
            is_not_exact_day, pos1 = checkImageneOnScreen(exactDayFail)
            if is_not_exact_day:
                # Si checkTrain es True, entonces verificar en el tren
                if checkTrain:
                    # Pasar al menú del tren
                    if findImageAndClick(trainMenu):
                        # Verificar que exista
                        is_capacity, position = checkImageneOnScreen(existCapacity)
                        if not is_capacity:
                            return False, False
                        else:
                            is_not_exact_day, pos1 = checkImageneOnScreen(exactDayFail)
                            if is_not_exact_day:
                                return False, False
                else:
                    return False, False

        # Si checkTrain es True, entonces verificar en el tren
        if not is_capacity:
            if checkTrain:
                # Pasar al menú del tren
                if findImageAndClick(trainMenu):
                    is_capacity, position = checkImageneOnScreen(existCapacity)
                    if not is_capacity:
                        return False, False
                    else:
                        return click_to_omnibus(capture, position)
            else:
                return False, False
        else:
            return click_to_omnibus(capture, position)
    return False, True
