from selectAsiento import select_asiento_varios
from pyautogui import sleep
from steep1SelectTrip import select_viaje
from utils import findImageAndClick, with_screen


def main(varios:bool, cantidad: int, exactDay:bool, checkTrain:bool, strongNotification:bool):
    is_capacity, fallo = select_viaje(exactDay, checkTrain)
    if is_capacity:
        return select_asiento_varios(cantidad, varios, strongNotification)
    else:
        btnAtras = f"./assets/{with_screen()}/btnAtras.png"
        findImageAndClick(btnAtras)
        sleep(0.2)

        if fallo:
            return False, True
        return False, False
def app(varios: bool = False, cantidad:int = 2, exactDay: bool = False, checkTrain: bool = True, strongNotification:bool = True):
    return main(varios, cantidad, exactDay, checkTrain, strongNotification)

if __name__ == '__main__':
    # window = 'Nox'
    # resizeWindow(window)
    # varios es para que escoja varios asientos, esta opcion funiona cuando concurency esta en False
    # aleatory es para que la repesca  no sea instantanea, sino que espere aleatoriamente para volver a hacer la peticion
    # cantidad son la cantidad de asientos que se kieren coger, funciona con la opcion varios en true
    # time es el tiempo maximo a esperar para refrescar va desde 1 hasta ese numero aleatoriamente
    # exactDay para que si no hay pasaejs para ese dia no coja el de otros
    # checkTrain verifica si hay pasajes en tren
    main(varios=True, cantidad=4, exactDay=False, checkTrain=True)