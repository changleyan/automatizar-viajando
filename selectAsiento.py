from utils import click, checkLoading, checkStay, sleep, distancy_between_points, locateAllOnScreen, region, center
from playsound import playsound

def select_asiento():
    asientoVacio = "./parts/asientos/asientov.png"
    asientoReservado = "./parts/asientos/asientor.png"
    btnSiguiente = "./parts/buttons/siguiente.png"

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

def select_asiento_varios(concurency: bool, cantidad: int, varios: bool):
    asientoVacio = "./parts/asientos/asientov.png"
    btnSiguiente = "./parts/buttons/btnSiguiente.png"

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
            print('Tenemos pasaje................')
            playsound("C:/Users/CHANG/WORK/viajando/automatizar-viajando/parts/notificacion.wav")
            return True

    return False