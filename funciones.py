from PyPDF2 import PdfReader
from datetime import datetime
import re
import os
from os import system
from palabra import *
#import xlsxwriter as xl


def menu():
    tamanio     = input("¿Cuántas palabras desea que tenga la oración?\n")
    referencia  = input("¿Dame la referencia para comenzar la oración?\n")
    probabilidad= input("Deseas que la probabilidad de selección de siguiente palabra sea:\n-A.Alta\n-B.Baja\n-M.Media\n")
    system("clear")
    return tamanio, referencia, probabilidad

def lector(inicio, fin):
    nombreLibro = "Harry_Potter"
    if(not os.path.isfile(nombreLibro + str(inicio) + str(fin) + ".txt")):
        reader = PdfReader(nombreLibro + ".pdf")
        for i in range(inicio,fin):
            page = reader.pages[i]
            pagina = page.extract_text()
            if i == inicio:
                libro = pagina
            else:
                libro = libro + " " + pagina
        file = open(nombreLibro + str(inicio) + str(fin) + ".txt", "w")
        libro = limpieza(libro)
        file.write(libro)
    else:
        file = open(nombreLibro + str(inicio) + str(fin) + ".txt", "r")
        libro = file.read()
    file.close()
    #escribe_bitacora("Se leyo el PDF y se extrajo el texto desde la página " +  str(inicio) + " hasta " + str(fin) + "\n")
    return libro

def limpieza(text):
    basura = "—-_'!¡¿?…:;«»()"
    text = text.lower()
    text = repar_palabras(text)
    text = ''.join(x for x in text if x not in basura)
    text = re.sub("\n"," ",text)
    text = re.sub("\t"," ",text)
    text = re.sub("  +"," ",text)
    text = repar_palabras(text)
    #escribe_bitacora("Se realizo la limpieza del texto.\n")
    return text

def repar_palabras(texto):
    texto = texto.replace(' v ', ' v')
    texto = texto.replace('llév atelo', 'llévatelo')
    texto = texto.replace('vuelv a', 'vuelva')
    texto = texto.replace('educativ a', 'educativa')
    texto = texto.replace('v oldemort', 'voldemort')
    texto = texto.replace(' y y a ', ' y a ')
    return texto

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
    pass
    #archivo = xl.Workbook('Base_datos.xlsx')
    #hoja=archivo.add_worksheet()
    #i = 0
    #for llave, valor in diccionario.items():
    #    hoja.write(i,0, llave)
    #    hoja.write(i,1, valor.num_ocurrencia+1)
    #    hoja.write(i,2, str(valor.tupla_sig_palabra))
    #    i+=1
    #archivo.close()

def p_base(base, texto, busqueda, dict):
    patron_n = busca_p(base, texto)
    if patron_n[0]:
        if busqueda+1 < len(texto):
            base.append(texto[busqueda])
            ayuda = p_base(base, texto, busqueda+1, dict)
            if ayuda[1]:
                meter = " ".join(base[:-1])
                if meter not in dict:
                    dict[meter] = patron_n[1]
                return busqueda-1, False, dict, patron_n[2]
            return ayuda
        else:
            return busqueda-1, False, dict
    else: #YA NO ES PATRON O NO FUE DESDE EL INICIO
        return busqueda-1, True, dict

def busca_p(list1, list2):
    indice1 = 0
    patron = 0
    indices_p = []
    for i in range(len(list2)):
        if list1[indice1] == list2[i]:
            aux = i
            for j in range(len(list1)):
                if list1[j] == list2[aux]:
                    indice1 += 1
                    if aux+1 <len(list2):
                        aux += 1
                else:
                    break
            if indice1 == len(list1):
                indices_p.append(aux-1)
                indice1 = 0
                patron += 1
            else:
                indice1 = 0
        else:
            continue
    if patron >= 10:
        return True, patron, indices_p
    else:
        return False, patron, indices_p

def func_main(texto):
    prueba = [0,False,{}]
    i=0
    li_li = []
    while i < len(texto):
        if i+2<len(texto):
            prueba = p_base([texto[i], texto[i+1]], texto, i+2, prueba[2])
            if len(prueba)==4 and prueba[3] not in li_li:
                li_li.append(prueba[3])

            i=prueba[0]
        else:
            i+=1
    print(prueba[2], li_li)