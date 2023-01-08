import funciones as fcf
import guis as gi

def main():

    textoSucio = fcf.lector(100,150)
    #4617 Paginas totales

    textoLimpio = fcf.limpieza(textoSucio)
    lista_palabras = fcf.separa_texto(textoLimpio)
    #dict = fcf.diccionario_palabras(lista_palabras)
    
    """
    valores_usuario = gi.ventana_Principal()

    if(valores_usuario[2] == "Probabilidad más alta"):
        aux = "a"
    elif(valores_usuario[2] == "Probabilidad intermedia"):
        aux = "m"
    elif(valores_usuario[2] == "Probabilidad más baja"):
        aux = "b"

    print("La longitud del texto es: ", int(valores_usuario[0]))
    print("La longitud de referencia es: ", int(valores_usuario[1]))
    print("La longitud de probabilidad: ", aux)
    print("La probabiliadad similar es: ", int(valores_usuario[3]))
    print("La referencia es: ", valores_usuario[4])
    
    textoFinal = fcf.crea_oracion(dict, valores_usuario[0], aux, valores_usuario[4])
    textoFinal = fcf.mejora_oracion(textoFinal)
    """
    #fcf.escribe_bitacora("La oracion final es: " + textoFinal)

main()