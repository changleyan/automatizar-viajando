from utils import click, checkLoading, checkStay, sleep, distancy_between_points, locateAllOnScreen, region, center, slideScreen
from playsound import playsound
from pathlib import Path
import simpleaudio as sa

def select_asiento():
    asientoVacio = "./assets/asientoVacio.png"
    asientoReservado = "./assets/asientoMarcado.png"
    btnSiguiente = "./assets/btnSiguiente.png"

    sleep(0.4)
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

def select_asiento_varios(concurency: bool, cantidad: int, varios: bool, strongNotification:bool, checkTrain:bool):
    asientoVacio = "./assets/asientoVacio.png"
    btnSiguiente = "./assets/btnSiguiente.png"

    # Verificar si existen asintos vacios entre los primeros asientos
    vacios = list(locateAllOnScreen(asientoVacio, region=region, confidence=0.85))
    total_aientos_vacios = restart = len(vacios)
    print(total_aientos_vacios, 'totallllll')
    print(vacios, 'vaciosssssss')
    if total_aientos_vacios == 0:
        # Verificar si existen asintos vacios entre los asientos del medio-final, se hace un slide para bajar
        slideScreen()
        sleep(0.3)
        vacios = list(locateAllOnScreen(asientoVacio, region=region, confidence=0.85))
        total_aientos_vacios = restart = len(vacios)
        print(total_aientos_vacios, 'totallllll2222222')
        if total_aientos_vacios == 0 and checkTrain:
            # Verificar si existen asintos vacios entre los asientos del final si es un tren, se hace un slide para bajar
            slideScreen()
            sleep(0.3)
            vacios = list(locateAllOnScreen(asientoVacio, region=region, confidence=0.85))
            total_aientos_vacios = restart = len(vacios)
            print(total_aientos_vacios, 'totallllll33333')

    if total_aientos_vacios == 0:
        # Si el total_aientos_vacios es 0 es pq no hay vacios
        return False, False

    cantidad = cantidad if (total_aientos_vacios > cantidad) else total_aientos_vacios

    # Para que coja uno solo de los que existan lo mas rapido posible
    if concurency or not varios:
        next = True
        while next:
            total_aientos_vacios -= 1
            position = center(vacios[total_aientos_vacios])
            click(position)
            if checkLoading() is False:
                sleep(0.2)
            next, nextPosition = checkStay(btnSiguiente)
            if next:
                next = False
            if total_aientos_vacios == 0:
                total_aientos_vacios = restart

    # Para que itere entre los asientos marcando varios
    else:
        while cantidad > 0:
            cantidad -= 1
            position = center(vacios[cantidad])
            click(position)
            if checkLoading() is False:
                sleep(0.3)

    #   Press btn Siguiente and notifi with sound
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
                    wave_obj = sa.WaveObject.from_wave_file(notification_route)
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
                    #playsound(notification_route)
            else:
                notification_route = "{}\\assets\\notificacion-lite.wav".format(Path().absolute()).replace(r"/","\"")
                wave_obj = sa.WaveObject.from_wave_file(notification_route)
                play_obj = wave_obj.play()
                play_obj.wait_done()
                #playsound(notification_route)
            return True, False

    return False, False