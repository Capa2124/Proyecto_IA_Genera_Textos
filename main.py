import funciones as fcf
import guis as gi

def main():
<<<<<<< HEAD
    textoSucio = fcf.lector(100,150)
=======
    #4617 Paginas totales
    textoSucio = fcf.lector(100,1000)
>>>>>>> 5e72cc47c1633fcc05a0df8b4f49c37f5c0cd73e
    textoLimpio = fcf.limpieza(textoSucio)
    lista_palabras = fcf.separa_texto(textoLimpio)
    #dict = fcf.diccionario_obj(lista_palabras)
    fcf.func_main(lista_palabras)
    
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
<<<<<<< HEAD
    

=======
    #gi.ventanaSecundariaConTexto(textoFinal)
>>>>>>> 5e72cc47c1633fcc05a0df8b4f49c37f5c0cd73e
    #fcf.escribe_bitacora("La oracion final es: " + textoFinal)

main()