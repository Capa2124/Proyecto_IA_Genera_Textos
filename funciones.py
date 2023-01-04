from PyPDF2 import PdfReader
from datetime import datetime
import re
from os import system
from palabra import *
import xlsxwriter as xl

def lector(inicio, fin):
    reader = PdfReader("Harry_Potter.pdf")
    for i in range(inicio,fin):
        page = reader.pages[i]
        pagina = page.extract_text()
        if i == inicio:
            libro = pagina
        else:
            libro = libro + " " + pagina
    escribe_bitacora("Se leyo el PDF y se extrajo el texto desde la página " +  str(inicio) + " hasta " + str(fin) + "\n")
    return libro

def limpieza(text):
    basura = "—-_'!¡¿?…:;.,«»()"
    text = ''.join(x for x in text if x not in basura)
    text = re.sub("\n"," ",text)
    text = re.sub("  +"," ",text)
    text = text.lower()
    #print(text)
    escribe_bitacora("Se realizo la limpieza del texto.\n")
    return text

def mejora_oracion(oracion):
    oracion = oracion.capitalize()
    #if oracion[:-1] == " ":
    oracion = oracion[:-1]
    oracion = oracion + "."

    escribe_bitacora("\nSe mejoro la oracion.\n")
    return oracion

def escribe_bitacora(registro):
    now = datetime.now()
    nombre_archivo = str(now.day) + '-' + str(now.month) + '-' + str(now.year) + '_' +  str(now.hour) + 'horas_' + str(now.minute) + 'minutos_'
    file = open(nombre_archivo + '.txt', "a")
    file.write(registro)
    file.close()

def separa_texto(texto):
    return texto.split(" ")

def diccionario_obj(lista):
    diccionario = {}
    for i in range(len(lista)-1):
        if lista[i] not in diccionario.keys():
            #print("Guarda", palabra)
            diccionario[lista[i]] = Palabra(lista[i])
        else:
            diccionario[lista[i]].num_ocurrencia += 1
        
        diccionario[lista[i]].agrega_sig_palabra(lista[i+1])
    
    for i in diccionario.keys():
        diccionario[i].cierra_tabla()
        
    escribe_bitacora("Se crea un diccionario con todas las palabras del texto y sus siguientes palabras.\n")
    return diccionario

def crea_oracion(diccionario, tamanio, probabilidad, referencia = "harry"):
    textoFinal = ""
    for i in range(int(tamanio)):
        escribe_bitacora("Referencia: " +  referencia + "  sig palabras: " + str(diccionario[referencia].tupla_sig_palabra) + "\n\n")
        textoFinal += referencia + " "
        aux = diccionario[referencia]
        referencia = aux.get_sig_palabra(probabilidad)
    return textoFinal

def crea_excel(diccionario):
    archivo = xl.Workbook('Base_datos.xlsx')
    hoja=archivo.add_worksheet()
    i = 0
    for llave, valor in diccionario.items():
        hoja.write(i,0, llave)
        hoja.write(i,1, valor.num_ocurrencia+1)
        hoja.write(i,2, str(valor.tupla_sig_palabra))
        i+=1
    archivo.close()  

def separa_texto(texto):
    return texto.split(" ")

def es_patron(texto, candidato_a_patron):
    aux = False
    if (texto.count(candidato_a_patron) >= 5):
        aux = True
    return aux  

def busca_patron(texto, tamanio):
    patrones = []
    lista_palabras = separa_texto(texto)
    i = 0
    while i < len(lista_palabras)-tamanio:
        candidato = str(lista_palabras[i])
        for j in range(i+1, i+tamanio):
            candidato += " "
            candidato += str(lista_palabras[j])        
        #en caso de ser patrón entonces se agrega a la lista de patrones
        if(es_patron(texto, candidato) and candidato not in patrones):
            #agrega_patron(texto, candidato)
            patrones.append(candidato)
            i += tamanio 
        #en caso contrario entonces buscamos con un nuevo conjunto de palabras   
        else:
            i += 1
    return patrones

def revicion_NuevoPatron(cadenaCorta, cadenaLarga):
    for i in cadenaLarga:
        for j in cadenaCorta:
            if (i.find(j) != -1):
                print(j)
                cadenaCorta.remove(j)
    cadenaLarga = cadenaLarga + cadenaCorta
    #Regresa la cadenaLarga junto a la cadenaCorta pero sin las cendeas que se repiten
    return cadenaLarga

def superPatrones(libro):
    patrones4 = busca_patron(libro, 4)
    patrones3 = busca_patron(libro, 3)
    patrones2 = busca_patron(libro, 2)
    patrones4y3 = revicion_NuevoPatron(patrones3,patrones4)
    superPat = revicion_NuevoPatron(patrones2,patrones4y3)
    return superPat

"""
def p_base(base, texto, busqueda, lista):
    if busca_p(base, texto)[0]:
        if busqueda < len(texto):
            base.append(texto[busqueda])
            p_base(base, texto, busqueda+len(base), lista)
        if base[:-1] not in lista:
            lista.append(base[:-1])
        return busqueda, lista
    else:
        if busqueda+len(base)<len(texto):
            busqueda += len(base)
        return busqueda, lista

def busca_p(list1, list2):
    indice1 = 0
    patron = 0
    indices_p = []
    for i in range(len(list2)):
        if list1[indice1] == list2[i]:
            aux = i
            for j in range(len(list1)):
                if list1[indice1] == list2[aux]:
                    indice1 += 1
                    aux += 1
                else:
                    break
            if indice1 == len(list1):
                indices_p.append(aux-len(list1))
                indice1 = 0
                patron += 1
            else:
                indice1 = 0
        else:
            continue

    if patron >= 3:
        return True, patron, indices_p
    else:
        return False, patron, indices_p
"""