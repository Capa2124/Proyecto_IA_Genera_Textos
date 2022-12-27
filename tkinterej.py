import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Mini Proyecto")
ventana.config(width=500, height=200)

TKpalabras = ttk.Label(text = "¿Cuántas palabras desea que tenga la oración?")
TKpalabras.place(x=20, y=20)

cajaTkpalbras = ttk.Entry()
cajaTkpalbras.place(x=270, y=40, width=60)

TKreferencia = ttk.Label(text = "¿Dame la referencia para comenzar la oración?")
TKreferencia.place(x=20, y=60)

cajaTkreferencia = ttk.Entry()
cajaTkreferencia.place(x=270, y=80, width=60)


TKprobabilidad = ttk.Label(text = "Deseas que la probabilidad de selección de siguiente palabra sea:")
TKprobabilidad.place(x=20, y=100)

grupoProba = tk.Frame(master=ventana, width=20, height=20)
cajaProbabilidad = tk.Listbox(master=grupoProba)
cajaProbabilidad.insert(tk.END, "Alta", "Media", "Baja")
grupoProba.pack()

botonGenera = ttk.Button(text="Convertir")
botonGenera.place(x=270, y=140)

ventana.mainloop()