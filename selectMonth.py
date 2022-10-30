from utils import *

def select_month(month:str):
    month = "./parts/meses/{}.png".format(month)
    nextMonth = "./parts/buttons/nextMonth.png"

    is_month, pos = checkStay(month)
    if is_month is False:
        if clickButton(nextMonth):
            return True
    else:
        return True
    return False
