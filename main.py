import tkinter as tk
import threading
from app import app
from pyautogui import sleep
from utils import resizeWindow
import random
import simpleaudio as sa

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Viajando Scraper')
        self.geometry("370x350+1000+300")

        # Estado iniciales
        self.varios = tk.IntVar(value=0)
        self.exactDay = tk.IntVar(value=0)
        self.checkTrain = tk.IntVar(value=0)
        self.strongNotification = tk.IntVar(value=0)

        self.create_checkbutton("Dia exacto", self.exactDay, 60, 30)
        self.create_checkbutton("Varios pasajes", self.varios, 60, 90)
        self.create_checkbutton("Verificar en tren", self.checkTrain, 60, 60)
        self.create_checkbutton("Repetir Notificación [5]", self.strongNotification, 60, 120)

        self.t1 = self.create_label_entry('Asientos [cantidad]', '2', 60, 170)
        self.t2 = self.create_label_entry('Refrescar en [seg]', '5', 60, 200)

        self.label = tk.Label(self, text="Detenido", font=('Helvetica 13'))
        self.label.place(x=60, y=240)

        self.stop_event = threading.Event()

        self.start_button = tk.Button(self, text="Start", command=self.start_thread)
        self.start_button.place(x=60, y=290)

        self.stop_button = tk.Button(self, text="Stop", command=self.stop)
        self.stop_button.place(x=120, y=290)

        self.exit_button = tk.Button(self, text="Exit", command=self.destroy)
        self.exit_button.place(x=180, y=290)

    def create_checkbutton(self, text, variable, x, y):
        checkbutton = tk.Checkbutton(self, text=text, variable=variable)
        checkbutton.place(x=x, y=y)

    def create_label_entry(self, text, default, x, y):
        label = tk.Label(self, text=text)
        label.place(x=x, y=y)
        entry = tk.Entry(self, width=10)
        entry.insert(tk.END, default)
        entry.place(x=x+180, y=y)
        return entry

    def start_thread(self):
        self.thread = threading.Thread(target=self.start)
        self.thread.start()

    def start(self):
        cantidad = int(self.t1.get())
        time = int(self.t2.get())

        self.stop_event.clear()

        # redimensionando la ventana para que coincidan las imagenes
        window = 'MEmu'
        resizeWindow(window)

        # contar los fallos del boton buscar, para ver si falla 5 vece y detener el ciclo
        fallos_permitidos = 5

        while True:
            self.label.config(text="Refrescando....", font=('Helvetica 13'))
            result, fallo = app(self.varios.get(), cantidad, self.exactDay.get(), self.checkTrain.get(),
                                self.strongNotification.get())
            if result or self.stop_event.is_set() or (fallo and fallos_permitidos <= 0):
                print("Stop")
                self.label.config(text="Escaner detenido", font=('Helvetica 13'))
                notification_route = "./assets/stoped.wav"
                print(notification_route, 'sdsd')
                notification_sound = sa.WaveObject.from_wave_file(notification_route)
                notification_sound.play().wait_done()
                break
            # ver si esta fallando al encontrar el buscar, esto kiere decir que o se cerro la app u ocurrio algun otro error
            if fallo:
                print(fallo, fallos_permitidos, 'fallos de la fallo')
                fallos_permitidos -= 1
            if not fallo:
                fallos_permitidos = 5
            # tiempo antes de volver a ejecutar
            cont = random.randrange(1, time)
            print("Refrescar en: " + str(cont))
            for _ in range(cont):
                self.label.config(text="Refrescar en: {} segundos".format(cont), font=('Helvetica 13'))
                cont -= 1
                sleep(1)
            self.label.config(text="Refrescando....", font=('Helvetica 13'))

    def stop(self):
        self.stop_event.set()

if __name__ == '__main__':
    appMain = Application()
    appMain.mainloop()
