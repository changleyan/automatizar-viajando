from selectAsiento import select_asiento_varios
from pyautogui import sleep
from steep1SelectTrip import select_viaje
from utils import findImageAndClick


def main(repesca: bool, concurency: bool, varios:bool, cantidad: int, capture: bool, exactDay:bool, checkTrain:bool, strongNotification:bool):
    is_capacity, fallo = select_viaje(capture, exactDay, checkTrain)
    if is_capacity:
        return select_asiento_varios(concurency, cantidad, varios, strongNotification)
    else:
        btnAtras = "./assets/btnAtras.png"
        findImageAndClick(btnAtras)
        sleep(0.2)

        if fallo:
            return False, True
        return False, False
def app(repesca: bool = True, concurency: bool = False, varios: bool = False, cantidad:int = 2, capture: bool = False, exactDay: bool = False, checkTrain: bool = True, strongNotification:bool = True):
    return main(repesca, concurency, varios, cantidad, capture, exactDay, checkTrain, strongNotification)

if __name__ == '__main__':
    # window = 'Nox'
    # resizeWindow(window)
    # repesca es para que cuando no vea omnibus disponibles vuelva a la pagian principal
    # concurrency es para que itere sobre los asientos hasta encontrar uno disponible (debe activarse a la hora pico 8:30)
    # varios es para que escoja varios asientos, esta opcion funiona cuando concurency esta en False
    # aleatory es para que la repesca  no sea instantanea, sino que espere aleatoriamente para volver a hacer la peticion
    # cantidad son la cantidad de asientos que se kieren coger, funciona con la opcion varios en true
    # time es el tiempo maximo a esperar para refrescar va desde 1 hasta ese numero aleatoriamente
    # capture para que capture los datos del omnibus que se seleciona
    # exactDay para que si no hay pasaejs para ese dia no coja el de otros
    # checkTrain verifica si hay pasajes en tren
    main(repesca=True, concurency=True, varios=True, cantidad=4, capture=True, exactDay=False, checkTrain=True)