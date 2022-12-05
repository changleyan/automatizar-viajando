from tkinter import *
from app import app
import threading
from pyautogui import sleep
from utils import resizeWindow
import random

window = Tk()

def variosListener():
    if varios.get():
        concurency.set(0)
    else:
        concurency.set(1)
def concurencyListener():
    if concurency.get():
        varios.set(0)
    else:
        varios.set(1)

# Estado iniciales
repesca = IntVar(value=1)
concurency = IntVar(value=0)
varios = IntVar(value=1)
aleatory = IntVar(value=1)
capture = IntVar(value=1)
exactDay = IntVar(value=0)
checkTrain = IntVar(value=1)
strongNotification = IntVar(value=0)


check_repesca = Checkbutton(window, text="Repesca", variable=repesca)
check_aleatory = Checkbutton(window, text="Respesca aleatoria", variable=aleatory)
check_concurency = Checkbutton(window, text="Concurrencia", variable=concurency, command=concurencyListener)
check_varios = Checkbutton(window, text="Varios pasajes", variable=varios, command=variosListener)
check_capture = Checkbutton(window, text="Capturar omnibus", variable=capture)
exact_day = Checkbutton(window, text="Dia exacto", variable=exactDay)
check_train = Checkbutton(window, text="Verificar en tren", variable=checkTrain)
strong_notification = Checkbutton(window, text="Notificacion fuerte", variable=strongNotification)

check_repesca.place(x=60, y=30)
check_aleatory.place(x=60, y=120)
check_concurency.place(x=60, y=60)
check_varios.place(x=60, y=90)
check_capture.place(x=60, y=150)
exact_day.place(x=60, y=180)
check_train.place(x=60, y=210)
strong_notification.place(x=60, y=240)


lbl1 = Label(window, text='Asientos')
lbl1.place(x=60, y=280)
t1=Entry()
t1.insert(END, '2')
t1.place(x=150, y=280)

lbl2 = Label(window, text='Refrescar')
lbl2.place(x=60, y=320)
t2=Entry()
t2.insert(END, '25')
t2.place(x=150, y=320)


label= Label(window, text="Refrescar en: 0 segundos", font=('Helvetica 13'))
label.place(x=50, y=430)

def start(stop):
    cantidad = int(t1.get())
    time = int(t2.get())

    global stop_threads
    stop_threads = False

    # redimensionando la ventana para que coincidan las imagenes
    window = 'Nox'
    resizeWindow(window)

    alternar = aleatory.get()
    while True:
        result = app(repesca.get(), concurency.get(), varios.get(), cantidad, capture.get(), exactDay.get(), checkTrain.get(), strongNotification.get())
        if result:
            print("Stop")
            label.config(text="Refrescar en: {} segundos".format(0), font=('Helvetica 13'))
            break
        # tiempo antes de volver a ejecutar
        timer = random.randrange(1, time) if alternar else 0
        print("Refrescar en: " + str(timer))
        label.config(text="Refrescar en: {} segundos".format(timer), font=('Helvetica 13'))
        sleep(timer)

        if stop():
            print("Stop")
            label.config(text="Refrescar en: {} segundos".format(0), font=('Helvetica 13'))
            break

stop_threads = False
def close():
    global stop_threads
    stop_threads = True
    print("Stopping threads..")


startbutton =Button(window,text="Start", command=lambda: threading.Thread(target=start, args=(lambda: stop_threads, )).start())
startbutton .place(x=50, y=370)

stopbutton =Button(window, text='Stop', command=close)
stopbutton .place(x=165, y=370)

exitbutton = Button(window, text="Exit", command=window.destroy)
exitbutton.place(x=280, y=370)


window.title('Viajando Scraper')
window.geometry("350x460+10+10")
window.mainloop()
