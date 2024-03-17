from utils import click, waitForLoadingOver, checkImageneOnScreen, sleep, findAllImages, slideScreen
from pathlib import Path
import simpleaudio as sa

def select_asiento_varios(concurency: bool, cantidad: int, varios: bool, strongNotification: bool):
    asientoVacio = "./assets/asientoVacio.png"
    btnSiguiente = "./assets/btnSiguiente.png"
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
    if concurency or not varios:
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
        for _ in range(cantidad):
            position = vacios.pop()
            click(position)
            if not waitForLoadingOver():
                sleep(0.3)

    if not waitForLoadingOver():
        next, nextPosition = checkImageneOnScreen(btnSiguiente)
        if next:
            click(nextPosition)
            print('Ta cogio................')
            notification_route = "{}\\assets\\notificacion-{}.wav".format(Path().absolute(), "strong" if strongNotification else "lite").replace(r"/","\"")
            notification_sound = sa.WaveObject.from_wave_file(notification_route)
            notification_sound.play().wait_done()
            return True, False

    return False, False
