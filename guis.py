import tkinter
from tkinter import *

def ventana_Principal():
    ventanaPrincipal = tkinter.Tk()
    ventanaPrincipal.title("Generador de textos empleando cadenas de Markov")
    ventanaPrincipal.geometry("400x200+700+400")

    value1 = tkinter.StringVar(ventanaPrincipal)
    value2 = tkinter.StringVar(ventanaPrincipal)
    value3 = tkinter.StringVar(ventanaPrincipal)
    value4 = tkinter.StringVar(ventanaPrincipal)
    value5 = tkinter.StringVar(ventanaPrincipal)

    #Texto y caja de longitud texto
    labelLogitudTexto = tkinter.Label(ventanaPrincipal, text = "Longitud del texto")
    labelLogitudTexto.pack()
    cajaLongitudTexto = tkinter.Entry(ventanaPrincipal, textvariable = value1)
    cajaLongitudTexto.pack()
    
    #Texto y caja longitud referncia
    labelLogitudReferencia = tkinter.Label(ventanaPrincipal, text = "Longitud de la referencia")
    labelLogitudReferencia.pack()
    cajaLongitudReferencia = tkinter.Entry(ventanaPrincipal, textvariable = value2)
    cajaLongitudReferencia.pack()

    #Texto y OpcionMenu para escoger la probabilidad de la referencia
    listaOpciones = ["Probabilidad más alta", "Probabilidad intermedia", "Probabilidad más baja"]
    ecogerSigReferencia = tkinter.Label(ventanaPrincipal, text = "Forma de escoger la siguiente referencia")
    ecogerSigReferencia.pack()
    value3.set("Selecciona una Opcion")
    menuProbablidad = tkinter.OptionMenu(ventanaPrincipal, value3, *listaOpciones)
    menuProbablidad.pack()

    #Texto y caja probabiliadad patrones similares
    probabilidadPatrones = tkinter.Label(ventanaPrincipal, text = "Probabilidad Patrones Similares")
    probabilidadPatrones.pack()
    cajaProbabilidadPatrones = tkinter.Entry(ventanaPrincipal, textvariable = value4)
    cajaProbabilidadPatrones.pack()

    #Texto y caja referencia Inicial
    referenciaInicial = tkinter.Label(ventanaPrincipal, text = "Referencia Inicial")
    referenciaInicial.pack()
    cajaReferenciaInicial = tkinter.Entry(ventanaPrincipal, textvariable = value5)
    cajaReferenciaInicial.pack()
    
    #Boton
    Boton = tkinter.Button(ventanaPrincipal, text='Enviar', command = ventanaPrincipal.destroy)
    Boton.pack()

    ventanaPrincipal.mainloop()
    return(value1.get(), value2.get(), value3.get(), value4.get(), value5.get())

def ventanaSecundariaConTexto(escrito):
    # Crear una ventana secundaria.
    ventanaTexto = tkinter.Tk()
    ventanaTexto.title("Generador de textos empleando cadenas de Markov")
    ventanaTexto.geometry("400x300+700+400")
    texto = tkinter.Label(ventanaTexto,text = escrito)
    texto.pack()
    texto.config(width = 50, height = 50)
    boton_cerrar = tkinter.Button(ventanaTexto, text = "Aceptar", command = ventanaTexto.destroy)
    boton_cerrar.pack()
    ventanaTexto.mainloop()