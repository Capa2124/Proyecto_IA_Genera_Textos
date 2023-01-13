import funciones as fcf
import guis as gi
import os

def main():

    path = os.path.dirname(os.path.abspath(__file__))
    path += "\Base_datos.xlsx"
    
    valores_usuario = gi.ventana_Principal()

    if(valores_usuario[1] == "Probabilidad más alta"):
        aux = "a"
    elif(valores_usuario[1] == "Probabilidad intermedia"):
        aux = "m"
    elif(valores_usuario[1] == "Probabilidad más baja"):
        aux = "b"
    
    

    if not os.path.isfile(path):
        textoSucio = fcf.lector(3000, 3050)
        #4617 pags totales
        textoLimpio = fcf.limpieza(textoSucio)
        lista_palabras = fcf.separa_texto(textoLimpio)
        print("Empezamos con busqueda de patrones")
        patrones_lista = fcf.busqueda_patrones(lista_palabras)
        print("terminamos busqueda de patrones")
        dicti = fcf.agrega_sig_elemento(lista_palabras,patrones_lista[1],patrones_lista[0])
        fcf.crea_excel(dicti)
        
        textoFinal = fcf.crea_Narrativa(patrones_lista[0], dicti, int(valores_usuario[0]), int(valores_usuario[2]), valores_usuario[3], aux)
        
    else:
        print("Encontramos archivo en ruta")
        dicti = fcf.lee_excel()
        print("Leo patrones de .txt")
        allPatrones = fcf.leePatrones()
        print("terminé...")
        textoFinal = fcf.crea_Narrativa(allPatrones, dicti, int(valores_usuario[0]), int(valores_usuario[2]), valores_usuario[3], aux)
    
    textoFinal = fcf.mejora_oracion(textoFinal)
    gi.ventanaSecundariaConTexto(textoFinal)
    

main()