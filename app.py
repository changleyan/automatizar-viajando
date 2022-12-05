# from selectInputFechaIda import select_input_fecha
# from selectMonth import select_month
# from selectDay import select_day
# import keyboard
from selectAsiento import select_asiento_varios
from pyautogui import sleep
from utils import clickButton, checkLoading, checkStay, slideScreen, pag, region, click
from datetime import datetime


# def refresh_fecha(month, day):
#     # buscar y seleccionar el boton de refrescar
#     input = select_input_fecha()
#     while input is False or keyboard.is_pressed('q'):
#         sleep(0.5)
#         input = select_input_fecha()
#     return select_month_day(month, day)
#
#
# def select_month_day(month, day):
#     btnAceptar = "./assets/aceptar.png"
#     btnCancelar = "./assets/cancelar.png"
#
#     if select_month(month):
#         # buscar y seleccionar dia
#         if select_day(day):
#             # buscar y seleccionar el boton de aceptar
#             clickButton(btnAceptar)
#             return True
#         else:
#             # cancelar, esperar 2 segundos y volver a buscar
#             clickButton(btnCancelar)
#             sleep(1)
#             refresh_fecha(month, day)
#     return False
#
#
# def step_1_select_day(month, day):
#     return refresh_fecha(month, day)


def click_to_omnibus(capture: bool, position):
    if capture:
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        ruta = "C:/Users/CHANG/Pictures/Pasajes/{}.png".format(ts)
        pag.screenshot(ruta, region=region)

    sleep(0.1)
    click(position)
    sleep(0.2)
    loading = checkLoading()
    sleep(0.1)
    if loading is False:
        return True
    return False

def select_viaje(capture: bool, exactDay: bool, checkTrain:bool):
    btnBuscar = "./assets/btnBuscar.png"        #boton de buscar
    exactDayFail = "./assets/exactDayFail.png"  #es el mensaje que sale cuando no hay pasajes para ese dia
    existCapacity = "./assets/btnOmnibus.png"   #es el mensaje que sale cuando no hay pasajes aunque no sea del dia
    trainMenu = "./assets/btnTren.png"          #boton del menu de tren

    if clickButton(btnBuscar):
        loading = checkLoading()
        if loading is False:
            position = None
            iscapacity, position = checkStay(existCapacity)
            if exactDay:
                # veo si no hay en omnibus
                isNotExactDay, pos1 = checkStay(exactDayFail)
                if isNotExactDay:
                    # si checkTrain es true entonces verifico en el tren
                    if checkTrain:
                        # paso al menu del tren
                        if clickButton(trainMenu):
                            # verifico que exista
                            iscapacity, position = checkStay(existCapacity)
                            if iscapacity is False:
                                return False
                            else:
                                isNotExactDay, pos1 = checkStay(exactDayFail)
                                if isNotExactDay:
                                    return False
                    else:
                        return False

            if iscapacity is False:
                # si checkTrain es true entonces verifico en el tren
                if checkTrain:
                    # paso al menu del tren
                    if clickButton(trainMenu):
                        iscapacity, position = checkStay(existCapacity)
                        if iscapacity is False:
                            return False
                        else:
                            return click_to_omnibus(capture, position)
                else:
                    return False
            else:
                return click_to_omnibus(capture, position)
    return False


def main(repesca: bool, concurency: bool, varios:bool, cantidad: int, capture: bool, exactDay:bool, checkTrain:bool, strongNotification:bool):
    is_capacity = select_viaje(capture, exactDay, checkTrain)
    if is_capacity:
        slideScreen()
        return select_asiento_varios(concurency, cantidad, varios, strongNotification)
    else:
        if repesca:
            btnAtras = "./assets/btnAtras.png"
            clickButton(btnAtras)
            checkLoading()
            return False
def app(repesca: bool = False, concurency: bool = False, varios: bool = False, cantidad:int = 2, capture: bool = False, exactDay: bool = False, checkTrain: bool = True, strongNotification:bool = True):
    return main(repesca, concurency, varios, cantidad, capture, exactDay, checkTrain, strongNotification)

if __name__ == '__main__':
    # window = 'Nox'
    # resizeWindow(window)
    # repesca es para que cuando no vea omnibus disponibles vuelva a la pagian principal
    # concurrency es para que itere sobre los asientos hasta encontrar uno disponible (debe activarse a la hora pico 8:30)
    # varios es para que escoja varios asientos, esta opcion funiona cuando concurency esta en False
    # aleatory es para que la repesca  no sea instantanea, sino que espere aleatoriamente para volver a hacer la peticion
    # cantidad son la cantidad de asientos que se kieren coger, funciona con la opcion varios en true
    # time es el tiempo maximo a esperar para refrescar va desde 1 hasta ese numero aleatoriamente
    # capture para que capture los datos del omnibus que se seleciona
    # exactDay para que si no hay pasaejs para ese dia no coja el de otros
    # checkTrain verifica si hay pasajes en tren
    main(repesca=True, concurency=True, varios=True, cantidad=4, capture=True, exactDay=False, checkTrain=True)