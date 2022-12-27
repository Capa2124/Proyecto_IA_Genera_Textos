import funciones as fcf

def main():
    #patron = "sangre sucia"
    textoS = fcf.lector(100,1000)
    textoL = fcf.limpieza(textoS)
    lista_palabras = fcf.separa_texto(textoL)
    #for i in range (len(lista_palabras)):
    #    if lista_palabras[i] == "sangre":
    #        if lista_palabras[i+1] == "sucia":
    #            print("sangre sucia "+ lista_palabras[i+2])
    print(len(lista_palabras))
    dict = fcf.diccionario_obj(lista_palabras)
    fcf.crea_excel(dict)
    tamanio, referencia, probabilidad = fcf.menu()
    textoFinal = fcf.crea_oracion(dict, tamanio, probabilidad, referencia)
    textoFinal = fcf.mejora_oracion(textoFinal)
    fcf.escribe_bitacora("La oracion final es: " + textoFinal)
    print(textoFinal)


main()