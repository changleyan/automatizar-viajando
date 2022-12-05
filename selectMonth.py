from utils import *

def select_month(month:str):
    month = "./assets/meses/{}.png".format(month)
    nextMonth = "./assets/nextMonth.png"

    is_month, pos = checkStay(month)
    if is_month is False:
        if clickButton(nextMonth):
            return True
    else:
        return True
    return False
