from utils import waitForLoadingOver, checkImageneOnScreen, click, findImageAndClick, with_screen
from pyautogui import sleep

def click_to_omnibus(position):
    sleep(0.2)
    click(position)
    sleep(0.2)
    waitForLoadingOver()
    sleep(0.2)
    return True, False

def select_viaje(exactDay: bool, checkTrain: bool):
    btnBuscar = f"./assets/{with_screen()}/btnBuscar.png"
    exactDayFail = f"./assets/{with_screen()}/exactDayFail.png"
    existCapacity = f"./assets/{with_screen()}/btnOmnibus.png"
    trainMenu = f"./assets/{with_screen()}/btnTren.png"

    if findImageAndClick(btnBuscar):
        waitForLoadingOver()

        is_capacity, position = checkImageneOnScreen(existCapacity)
        if not is_capacity and checkTrain:
            if findImageAndClick(trainMenu):
                is_capacity, position = checkImageneOnScreen(existCapacity)
                if not is_capacity:
                    return False, False

        if exactDay:
            is_not_exact_day, _ = checkImageneOnScreen(exactDayFail)
            if is_not_exact_day and not checkTrain:
                return False, False
            if is_not_exact_day and checkTrain:
                if findImageAndClick(trainMenu):
                    is_not_exact_day, _ = checkImageneOnScreen(exactDayFail)
                    if is_not_exact_day:
                        return False, False
                    is_capacity, position = checkImageneOnScreen(existCapacity)
                    if not is_capacity:
                        return False, False

        if is_capacity:
            return click_to_omnibus(position)

    return False, True
