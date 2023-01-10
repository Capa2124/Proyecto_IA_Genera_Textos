import funciones as fcf
import guis as gi
import os

def main():
    valores = [100,12,"a",50,"la profesora"]

    path = os.path.dirname(os.path.abspath(__file__))
    path += "\Base_datos.xlsx"

    if not os.path.isfile(path):
        textoSucio = fcf.lector(300,500)
        #4617 pags totales
        textoLimpio = fcf.limpieza(textoSucio)
        lista_palabras = fcf.separa_texto(textoLimpio)
        patrones_lista = fcf.busqueda_patrones(lista_palabras)
        dicti = fcf.agrega_sig_elemento(lista_palabras,patrones_lista[1],patrones_lista[0])
        fcf.crea_excel(dicti)
        textoFinal = fcf.crea_Narrativa(patrones_lista[0], dicti, valores[0], valores[3], valores[4], valores[2])
        print(textoFinal)
    else:
        print("Encontramos archivo en ruta")
        dicti = fcf.lee_excel()    
        allPatrones = fcf.leePatrones()
        textoFinal = fcf.crea_Narrativa(allPatrones, dicti, valores[0], valores[3], valores[4], valores[2])
        print(textoFinal)
        #print(dicti)
        #print(dicti["jugadores"].tupla_sig_palabra)
    
    #print("Prueba: ", dicti["mcgonagall"].tupla_sig_patron[0])
    #print("Imprimo tupla_sig_patron[0]: ", dicti["mcgonagall"].tupla_sig_patron[0])
    #print("Imprimo tupla_sig_patron[0][1]: ", dicti["mcgonagall"].tupla_sig_patron[0][1])
    #print(dicti["mcgonagall"].get_sig_palabra(valores[2]))

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