from tkinter import *
from app import main

window = Tk()

# Estado iniciales
repesca = IntVar(value=1)
concurency = IntVar(value=1)
varios = IntVar(value=0)
aleatory = IntVar(value=1)
capture = IntVar(value=1)


check_repesca = Checkbutton(window, text="Repesca", variable=repesca)
check_aleatory = Checkbutton(window, text="Respesca aleatoria", variable=aleatory)
check_concurency = Checkbutton(window, text="Concurrencia", variable=concurency)
check_varios = Checkbutton(window, text="Varios pasajes", variable=varios)
check_capture = Checkbutton(window, text="Capturar omnibus", variable=capture)

check_repesca.place(x=60, y=30)
check_aleatory.place(x=60, y=120)
check_concurency.place(x=60, y=60)
check_varios.place(x=60, y=90)
check_capture.place(x=60, y=150)


lbl1 = Label(window, text='Asientos')
lbl1.place(x=60, y=200)
t1=Entry()
t1.insert(END, '2')
t1.place(x=150, y=200)

lbl2 = Label(window, text='Refrescar')
lbl2.place(x=60, y=250)
t2=Entry()
t2.insert(END, '25')
t2.place(x=150, y=250)

def find():
    cantidad = int(t1.get())
    time = int(t2.get())
    main(repesca.get(), concurency.get(), varios.get(), aleatory.get(), cantidad, time, capture.get())

def close():
    quit()
    exit()

b1=Button(window, text='Buscar', command=find)
b1.place(x=120, y=300)

b2=Button(window, text='Stop', command=close)
b2.place(x=200, y=300)


window.title('Viajando App')
window.geometry("350x400+10+10")
window.mainloop()
