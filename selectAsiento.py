from utils import click, checkLoading, checkStay, sleep, distancy_between_points, locateAllOnScreen, region, center
from playsound import playsound
from pathlib import Path

def select_asiento():
    asientoVacio = "./assets/asientoVacio.png"
    asientoReservado = "./assets/asientoMarcado.png"
    btnSiguiente = "./assets/btnSiguiente.png"

    vacio, vacioPosition = checkStay(asientoVacio)
    if vacio:
        click(vacioPosition)
        sleep(0.2)
        loading = checkLoading()
        if loading is False:
            reservado, reservadoPosition = checkStay(asientoReservado)
            distancia = distancy_between_points(vacioPosition, reservadoPosition)
            if checkLoading() is False:
                if reservado and distancia <= 5:

                    next, nextPosition = checkStay(btnSiguiente)
                    if next:
                        click(nextPosition)
                        print('Urra, tenemos pasaje................')
                        return True
    return False


def select_varios_aux():
    pass

def select_asiento_varios(concurency: bool, cantidad: int, varios: bool, strongNotification:bool):
    asientoVacio = "./assets/asientoVacio.png"
    btnSiguiente = "./assets/btnSiguiente.png"

    vacios = list(locateAllOnScreen(asientoVacio, region=region, confidence=0.9))
    total = restart = len(vacios)
    cantidad = cantidad if (total > cantidad) else total

    if concurency or not varios:
        next = True
        while next:
            total -= 1
            position = center(vacios[total])
            click(position)
            if checkLoading() is False:
                sleep(0.1)
            next, nextPosition = checkStay(btnSiguiente)
            if next:
                next = False
            if total == 0:
                total = restart

    else:
        while cantidad > 0:
            cantidad -= 1
            position = center(vacios[cantidad])
            click(position)
            if checkLoading() is False:
                sleep(0.1)
    if checkLoading() is False:
        next, nextPosition = checkStay(btnSiguiente)
        if next:
            click(nextPosition)
            print('Ta cogio................')
            if strongNotification:
                notification_route = "{}\\assets\\notificacion-strong.wav".format(Path().absolute()).replace(r"/","\"")
                cant = 10
                while cant > 0:
                    cant -= 1
                    playsound(notification_route)
            else:
                notification_route = "{}\\assets\\notificacion-lite.wav".format(Path().absolute()).replace(r"/","\"")
                playsound(notification_route)
            return True

    return False