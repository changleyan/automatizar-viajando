import pyautogui as pag
import pyautogui
import time
import win32con
import win32api
import pygetwindow
import math
import cv2
from pyautogui import sleep
import numpy as np

region = (0, 3, 429, 724)

def click(position):
    win32api.SetCursorPos(position)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def find_image_position(image_path):
    # Load the image to search for
    imagen_a_buscar = cv2.imread(image_path)

    # Capture the screen using pyautogui
    pantalla = pyautogui.screenshot()

    # Convert the screenshot to OpenCV format
    pantalla = cv2.cvtColor(np.array(pantalla), cv2.COLOR_RGB2BGR)

    # Find the position of the image on the screen
    resultado = cv2.matchTemplate(pantalla, imagen_a_buscar, cv2.TM_SQDIFF_NORMED)

    # Get the minimum value from the result
    min_val, _, min_loc, _ = cv2.minMaxLoc(resultado)

    # If the minimum value is greater than a certain threshold, the image is not found
    if min_val > 0.2:  # You may need to adjust this threshold based on your images and use case
        print("Image not found!")
        return None

    # Get the coordinates of the top-left corner of the match
    x = min_loc[0] + int(imagen_a_buscar.shape[1] / 2)
    y = min_loc[1] + int(imagen_a_buscar.shape[0] / 2)

    return (x, y)

def cehckImagenInScreen(imagen: str):
    # Load the image to search for
    imagen_a_buscar = cv2.imread(imagen)

    # Capture the screen using pyautogui
    pantalla = pyautogui.screenshot()

    # Convert the screenshot to OpenCV format
    pantalla = cv2.cvtColor(np.array(pantalla), cv2.COLOR_RGB2BGR)

    # Find the position of the image on the screen
    resultado = cv2.matchTemplate(pantalla, imagen_a_buscar, cv2.TM_SQDIFF_NORMED)

    # Get the minimum value from the result
    min_val = cv2.minMaxLoc(resultado)[0]

    # If the minimum value is greater than a certain threshold, the image is not found
    if min_val > 0.2:  # You may need to adjust this threshold based on your images and use case
        print("Image not found!")
        return False
    return True

def isLoadindOnScreen(imagen: str):
    # Preprocesamiento de la imagen
    imagen_a_buscar = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)
    _, imagen_a_buscar = cv2.threshold(imagen_a_buscar, 127, 255, cv2.THRESH_BINARY)
    imagen_a_buscar = np.uint8(imagen_a_buscar)  # Convertir a tipo CV_8U

    # Captura la pantalla
    pantalla = pyautogui.screenshot()
    pantalla = cv2.cvtColor(np.array(pantalla), cv2.COLOR_RGB2BGR)
    pantalla = cv2.cvtColor(pantalla, cv2.COLOR_BGR2GRAY)
    pantalla = np.uint8(pantalla)  # Convertir a tipo CV_8U

    # Realiza la búsqueda de la plantilla de la imagen
    resultado = cv2.matchTemplate(pantalla, imagen_a_buscar, cv2.TM_CCOEFF_NORMED)

    # Establece un umbral para filtrar las detecciones
    threshold = 0.8
    loc = np.where(resultado >= threshold)

    # Filtra las detecciones para eliminar falsos positivos
    for pt in zip(*loc[::-1]):
        # Verifica el contexto alrededor de la detección (por ejemplo, busca ciertos elementos cercanos)
        # Realiza acciones adicionales según sea necesario
        return True
    return False

def waitForLoadingOver(imagen: str = "./assets/genericLoader.png"):
    position = isLoadindOnScreen(imagen)
    while position:
        sleep(0.4)
        position = isLoadindOnScreen(imagen)
    sleep(0.3)
    return False





def checkImageneOnScreen(imagen: str):
    position = find_image_position(imagen)
    sleep(0.2)
    if position is None:
        return False, None
    return True, position

def slideScreen():
    print('Slide...')
    sleep(0.2)
    pag.moveTo(190,645, duration=0.1)
    pag.dragTo(190,210, button='left', duration=0.1)
    sleep(0.2)

def resizeWindow(nameWindow):
    win = pygetwindow.getWindowsWithTitle(nameWindow)[0]
    win.moveTo(0, 3)
    win.size = (429, 724)
    return True

def distancy_between_points(p1, p2):
    distancia = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
    return round(distancia)

def findImageAndClick(imagen: str):
    # find position of imagen
    position = find_image_position(imagen)

    # Move the mouse and click at the position of the match
    pyautogui.moveTo(position)
    pyautogui.click()
    sleep(0.2)
    return True

def findAllImages(image_path: str, threshold=0.8, min_distance=5):
    # Cargar la imagen a buscar
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Capturar la pantalla usando pyautogui
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    # Realizar la coincidencia de la plantilla
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

    # Encontrar las posiciones donde la coincidencia es mayor que el umbral dado
    locations = np.where(result >= threshold)

    # Filtrar las posiciones para evitar detecciones demasiado cercanas
    filtered_locations = []
    for loc in zip(*locations[::-1]):
        # Comprobar la distancia mínima con otras detecciones
        if all(cv2.norm(np.array(loc) - np.array(existing_loc)) > min_distance for existing_loc in filtered_locations):
            filtered_locations.append(loc)

    # Calcular el centro de cada detección
    centers = [(x + template.shape[1] // 2, y + template.shape[0] // 2) for x, y in filtered_locations]

    return centers
