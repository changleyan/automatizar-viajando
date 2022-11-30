from selectInputFechaIda import select_input_fecha
from selectMonth import select_month
from selectDay import select_day
from selectAsiento import select_asiento, select_asiento_varios
from pyautogui import sleep, prompt
from utils import clickButton, checkLoading, checkStay, slideScreen, resizeWindow, pag, region
import keyboard, random
from datetime import datetime


def refresh_fecha(month, day):
    # buscar y seleccionar el boton de refrescar
    input = select_input_fecha()
    while input is False or keyboard.is_pressed('q'):
        sleep(0.5)
        input = select_input_fecha()
    return select_month_day(month, day)


def select_month_day(month, day):
    btnAceptar = "./parts/buttons/aceptar.png"
    btnCancelar = "./parts/buttons/cancelar.png"

    if select_month(month):
        # buscar y seleccionar dia
        if select_day(day):
            # buscar y seleccionar el boton de aceptar
            clickButton(btnAceptar)
            return True
        else:
            # cancelar, esperar 2 segundos y volver a buscar
            clickButton(btnCancelar)
            sleep(1)
            refresh_fecha(month, day)
    return False


def step_1_select_day(month, day):
    return refresh_fecha(month, day)


def select_omnibus():
    btnOmnibus = "./parts/buttons/nextOmnibus.png"
    sleep(0.1)
    clickButton(btnOmnibus)
    loading = checkLoading(btnOmnibus)
    sleep(0.1)
    if loading is False:
        return True
    return False


def step_2_select_viaje(capture: bool):
    btnBuscar = "./parts/buttons/buscar.png"
    noCapacity = "./parts/omnibus/noHayPasaje.png"
    serverError = "./parts/omnibus/errorServidor.png"
    serverFailConexion = "./parts/omnibus/noConexion.png"

    if clickButton(btnBuscar):
        loading = checkLoading()
        if loading is False:
            iscapacity, pos = checkStay(noCapacity)
            error, pos1 = checkStay(serverError)
            errorConexion, pos1 = checkStay(serverFailConexion)
            if iscapacity or error or errorConexion:
                print('No hay pasajes....!')
                return False
            else:
                if capture:
                    dt = datetime.now()
                    ts = datetime.timestamp(dt)
                    ruta = "C:/Users/CHANG/Pictures/Pasajes/{}.png".format(ts)
                    pag.screenshot(ruta, region=region)
                if select_omnibus():
                    return True
    return False


def step_3_select_asiento(varios: bool = False, concurency: bool = False,  cantidad : int = 2):
    return select_asiento_varios(concurency, cantidad, varios)


def main_aux(repesca: bool, concurency: bool, varios:bool, aleatory: bool, cantidad: int, time: int, capture: bool):
    is_capacity = step_2_select_viaje(capture)
    if is_capacity:
        slideScreen()
        step_3_select_asiento(varios, concurency, cantidad)
    else:
        if repesca:
            timer = random.randrange(1, time) if aleatory else 0
            print("Refrescar en: " + str(timer))
            sleep(timer)
            btnAtras = "./parts/buttons/btnAtras.png"
            clickButton(btnAtras)
            checkLoading()
            main(repesca, concurency, varios, aleatory, cantidad, time, capture)

def main(repesca: bool = False, concurency: bool = False, varios: bool = False, aleatory: bool = False, cantidad:int = 2, time:int = 10, capture: bool = False):
    if repesca:
        main_aux(repesca, concurency, varios, aleatory, cantidad, time, capture)
    else:
        month = 'Noviembre'
        day = prompt(text="", title="Entre el dia a buscar.")
        if day is not None:
            step_1_select_day(month, day)
            main_aux(repesca, concurency, varios, aleatory, cantidad, time, capture)

def app(repesca: bool = False, concurency: bool = False, varios: bool = False, aleatory: bool = False, cantidad:int = 2, time:int = 10, capture: bool = False):
    window = 'Nox'
    resizeWindow(window)
    main(repesca, concurency, varios, aleatory, cantidad, time, capture)


if __name__ == '__main__':
    window = 'Nox'
    resizeWindow(window)
    # repesca es para que cuando no vea omnibus disponibles vuelva a la pagian principal
    # concurrency es para que itere sobre los asientos hasta encontrar uno disponible (debe activarse a la hora pico 8:30)
    # varios es para que escoja varios asientos, esta opcion funiona cuando concurency esta en False
    # aleatory es para que la repesca  no sea instantanea, sino que espere aleatoriamente para volver a hacer la peticion
    # cantidad son la cantidad de asientos que se kieren coger, funciona con la opcion varios en true
    # time es el tiempo maximo a esperar para refrescar va desde 1 hasta ese numero aleatoriamente
    # capture para que capture los datos del omnibus que se seleciona
    main(repesca=True, concurency=True, varios=True, aleatory=True, cantidad=4, time=40, capture=True)