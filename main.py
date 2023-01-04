import funciones as fcf
import guis as gi

def main():
    #4617 Paginas totales
    textoSucio = fcf.lector(100,1000)
    textoLimpio = fcf.limpieza(textoSucio)
    lista_palabras = fcf.separa_texto(textoLimpio)
    dict = fcf.diccionario_obj(lista_palabras)

    #SECCION DE LECTURA DE LIBRO PARA BUSQUEDA DE PATRON#
    #fcf.busca_patron(lista_palabras)
    #fcf.es_patron()
    
    #fcf.crea_excel(dict)
    
    #Paso de los parametros por el usuario
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
    #gi.ventanaSecundariaConTexto(textoFinal)
    #fcf.escribe_bitacora("La oracion final es: " + textoFinal)

main()