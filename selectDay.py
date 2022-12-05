from utils import *

def select_day(day:str):
    day = "./assets/days/{}.png".format(day)
    if clickButton(day, 0.99):
        return True
    return False
