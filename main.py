from selectInputFechaIda import select_input_fecha
from selectMonth import select_month
from selectDay import select_day
from selectAsiento import select_asiento, select_asiento_varios
from pyautogui import sleep, prompt
from utils import clickButton, checkLoading, checkStay, slideScreen, resizeWindow, locateAllOnScreen, region, center, click
import keyboard


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

    if clickButton(btnBuscar):
        loading = checkLoading()
        if loading is False:
            iscapacity, pos = checkStay(noCapacity)
            if iscapacity:
                print('No hay ni pinga socio, claro si vives en el pais de pinga este....!')
                # hacer ciclo para volver al inicio
            else:
                if select_omnibus():
                    return True
    return False


def step_3_select_asiento(varios: bool = False, cantidad : int = 2):
    print("Step 3", varios, cantidad)
    return select_asiento_varios(cantidad) if varios else select_asiento()


def main():
    month = 'Noviembre'
    window = 'Nox'
    day = prompt(text="", title="Entre el dia a buscar.")

    if day is not None:
        resizeWindow(window)

        is_day = step_1_select_day(month, day)

        is_capacity = step_2_select_viaje()
        if is_capacity:
            slideScreen()
            step_3_select_asiento(True, 6)

if __name__ == '__main__':
    main()