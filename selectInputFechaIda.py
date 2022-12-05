from utils import *

#  funcion para pinchar el boton refrescar y seleccionar el input de fechaIda
def select_input_fecha():
    refresh = "./assets/refresh.PNG"
    input = "./assets/inputs/fechaIda.png"
    load = "./assets/genericLoader.png"

    if clickButton(refresh):
        loading = checkLoading(load)
        if loading is False:
            if clickButton(input, 0.8):
                return True
    return False

