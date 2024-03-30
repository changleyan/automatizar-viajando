from utils import click, waitForLoadingOver, checkImageneOnScreen, sleep, findAllImages, slideScreen, with_screen
from pathlib import Path
import simpleaudio as sa

def select_asiento_varios(cantidad: int, varios: bool, strongNotification: bool):
    asientoVacio = f"./assets/{with_screen()}/asientoVacio.png"
    btnSiguiente = f"./assets/{with_screen()}/btnSiguiente.png"
    def encontrar_asientos_vacios():
        vacios = list(findAllImages(asientoVacio))
        if len(vacios) == 0:
            slideScreen()
            sleep(0.2)
            vacios = list(findAllImages(asientoVacio))
        return vacios

    vacios = encontrar_asientos_vacios()
    total = restart = len(vacios)

    if total == 0:
        return False, False

    cantidad = min(cantidad, total)
    if not varios:
        while total > 0:
            total -= 1
            position = vacios[total]
            click(position)
            if not waitForLoadingOver():
                sleep(0.2)
            next, nextPosition = checkImageneOnScreen(btnSiguiente)
            if next:
                total = restart
                break

    else:
        vacios.reverse()
        for _ in range(cantidad):
            position = vacios.pop()
            click(position)
            sleep(0.3)
            if not waitForLoadingOver():
                sleep(0.3)

    if not waitForLoadingOver():
        next, nextPosition = checkImageneOnScreen(btnSiguiente)
        if next:
            click(nextPosition)
            print('Ta cogio................')
            notification_route = "{}\\assets\\notificacion-{}.wav".format(Path().absolute(), "lite").replace(r"/","\"")
            if strongNotification:
                cantNotificacion = 5
                while(cantNotificacion > 0):
                    notification_sound = sa.WaveObject.from_wave_file(notification_route)
                    notification_sound.play().wait_done()
                    cantNotificacion -= 1
            notification_sound = sa.WaveObject.from_wave_file(notification_route)
            notification_sound.play().wait_done()
            return True, False

    return False, False
