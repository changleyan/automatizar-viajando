from numpy import var

from selectInputFechaIda import select_input_fecha
from selectMonth import select_month
from selectDay import select_day
from selectAsiento import select_asiento, select_asiento_varios
from pyautogui import sleep, prompt
from utils import clickButton, checkLoading, checkStay, slideScreen, resizeWindow
import keyboard, random


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


def step_2_select_viaje():
    btnBuscar = "./parts/buttons/buscar.png"
    noCapacity = "./parts/omnibus/noHayPasaje.png"
    serverError = "./parts/omnibus/errorServidor.png"

    if clickButton(btnBuscar):
        loading = checkLoading()
        if loading is False:
            iscapacity, pos = checkStay(noCapacity)
            error, pos = checkStay(serverError)
            if iscapacity or error:
                # print('No hay ni pinga socio, claro si vives en el pais de pinga este....!')
                print('No hay pasajes....!')
                return False
            else:
                if select_omnibus():
                    return True
    return False


def step_3_select_asiento(varios: bool = False, concurency: bool = False,  cantidad : int = 2):
    print("Step 3", varios, cantidad)
    return select_asiento_varios(concurency, cantidad) if varios else select_asiento()


def main_aux(repesca: bool, concurency: bool, varios:bool, aleatory: bool, cantidad: int):
    is_capacity = step_2_select_viaje()
    if is_capacity:
        slideScreen()
        step_3_select_asiento(varios, concurency, cantidad)
    else:
        if repesca:
            timer = random.randrange(5, 15) if aleatory else 0
            print("Refrescar en: " + str(timer))
            sleep(timer)
            btnAtras = "./parts/buttons/btnAtras.png"
            clickButton(btnAtras)
            checkLoading()
            main(repesca, concurency, varios, aleatory, cantidad)

def main(repesca: bool = False, concurency: bool = False, varios: bool = False, aleatory: bool = False, cantidad:int = 2):
    if repesca:
        main_aux(repesca, concurency, varios, aleatory, cantidad)
    else:
        month = 'Noviembre'
        day = prompt(text="", title="Entre el dia a buscar.")
        if day is not None:
            step_1_select_day(month, day)
            main_aux(repesca, concurency, varios, aleatory, cantidad)


if __name__ == '__main__':
    window = 'Nox'
    resizeWindow(window)
    main(repesca=True, concurency=True, varios=True, aleatory=True, cantidad=4)