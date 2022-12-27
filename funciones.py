from PyPDF2 import PdfReader
from datetime import datetime
import re
from os import system
from palabra import *
import xlsxwriter as xl


def menu():
    tamanio     = input("¿Cuántas palabras desea que tenga la oración?\n")
    referencia  = input("¿Dame la referencia para comenzar la oración?\n")
    probabilidad= input("Deseas que la probabilidad de selección de siguiente palabra sea:\n-A.Alta\n-B.Baja\n-M.Media\n")
    system("clear")
    return tamanio, referencia, probabilidad

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
    textoF = ""
    for i in range(int(tamanio)):
        escribe_bitacora("Referencia: " +  referencia + "  sig palabras: " + str(diccionario[referencia].tupla_sig_palabra) + "\n\n")
        textoF += referencia + " "
        aux = diccionario[referencia]
        referencia = aux.get_sig_palabra(probabilidad)
    return textoF

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