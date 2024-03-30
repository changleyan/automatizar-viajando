import tkinter as tk
import threading
from app import app
from pyautogui import sleep
from utils import resizeWindow
import random

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Viajando Scraper')
        self.geometry("380x410+1000+300")

        # Estado iniciales
        self.varios = tk.IntVar(value=0)
        self.aleatory = tk.IntVar(value=1)
        self.capture = tk.IntVar(value=1)
        self.exactDay = tk.IntVar(value=0)
        self.checkTrain = tk.IntVar(value=0)
        self.strongNotification = tk.IntVar(value=0)

        self.create_checkbutton("Respesca aleatoria", self.aleatory, 60, 30)
        self.create_checkbutton("Varios pasajes", self.varios, 60, 90)
        self.create_checkbutton("Capturar omnibus", self.capture, 60, 60)
        self.create_checkbutton("Dia exacto", self.exactDay, 60, 120)
        self.create_checkbutton("Verificar en tren", self.checkTrain, 60, 150)
        self.create_checkbutton("Repetir Notificación [6]", self.strongNotification, 60, 180)

        self.lbl1 = tk.Label(self, text='Asientos')
        self.lbl1.place(x=60, y=220)
        self.t1 = tk.Entry(self)
        self.t1.insert(tk.END, '2')
        self.t1.place(x=150, y=220)

        self.lbl2 = tk.Label(self, text='Refrescar')
        self.lbl2.place(x=60, y=260)
        self.t2 = tk.Entry(self)
        self.t2.insert(tk.END, '5')
        self.t2.place(x=150, y=260)

        self.label = tk.Label(self, text="Detenido", font=('Helvetica 13'))
        self.label.place(x=50, y=300)

        self.stop_event = threading.Event()

    def create_checkbutton(self, text, variable, x, y):
        checkbutton = tk.Checkbutton(self, text=text, variable=variable)
        checkbutton.place(x=x, y=y)

    def start(self):
        cantidad = int(self.t1.get())
        time = int(self.t2.get())

        self.stop_event.clear()

        # redimensionando la ventana para que coincidan las imagenes
        window = 'MEmu'
        resizeWindow(window)

        # contar los fallos del boton buscar, para ver si falla 5 vece y detener el ciclo
        fallos_permitidos = 5

        alternar = self.aleatory.get()
        while True:
            self.label.config(text="Refrescando....", font=('Helvetica 13'))
            result, fallo = app(self.varios.get(), cantidad, self.capture.get(), self.exactDay.get(), self.checkTrain.get(),
                                self.strongNotification.get())
            if result:
                print("Stop")
                self.label.config(text="Refrescar en: {} segundos".format(0), font=('Helvetica 13'))
                break
            # ver si esta fallando al encontrar el buscar, esto kiere decir que o se cerro la app u ocurrio algun otro error
            if fallo:
                print(fallo, fallos_permitidos, 'fallos de la fallo')
                if fallos_permitidos <= 0:
                    print("Stop")
                    self.label.config(text="Refrescar en: {} segundos".format(0), font=('Helvetica 13'))
                    break
                fallos_permitidos -= 1
            if not fallo:
                fallos_permitidos = 5
            # tiempo antes de volver a ejecutar
            cont = random.randrange(1, time) if alternar else 0
            print("Refrescar en: " + str(cont))
            cont -= 1
            while cont > 0:
                self.label.config(text="Refrescar en: {} segundos".format(cont), font=('Helvetica 13'))
                cont -= 1
                sleep(1)
            self.label.config(text="Refrescando....", font=('Helvetica 13'))
            if self.stop_event.is_set():
                print("Stop")
                self.label.config(text="Detenido", font=('Helvetica 13'))
                break

    def close(self):
        self.stop_event.set()

    def run(self):
        startbutton = tk.Button(self, text="Start", command=lambda: threading.Thread(target=self.start).start())
        startbutton.place(x=50, y=350)

        stopbutton = tk.Button(self, text='Stop', command=self.close)
        stopbutton.place(x=165, y=350)

        exitbutton = tk.Button(self, text="Exit", command=self.destroy)
        exitbutton.place(x=280, y=350)

        self.mainloop()

if __name__ == "__main__":
    application = Application()
    application.run()

