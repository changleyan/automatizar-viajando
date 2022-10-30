from utils import click, checkLoading, checkStay, sleep, distancy_between_points, locateAllOnScreen, region, center

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


def select_asiento_varios(cantidad:int = 1):
    asientoVacio = "./parts/asientos/asientov.png"
    btnSiguiente = "./parts/buttons/siguiente.png"

    vacios = list(locateAllOnScreen(asientoVacio, region=region, confidence=0.9))
    cantidad = cantidad if (len(vacios) > cantidad) else len(vacios)

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
            print('Urra, tenemos pasaje................')
            return True

    return False