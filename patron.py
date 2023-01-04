import operator
import random

class Patron:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.num_ocurrencia    = 0
        self.num_sig_palabra   = 0
        self.diccionario_sig_palabra = {}
        self.tupla_sig_palabras = ()
        self.diccionario_sig_patron = {}
        self.tupla_sig_patrones = ()
    
    def agrega_sig_palabra(self, sig_palabra):
        if sig_palabra in self.diccionario_sig_palabra.keys():
            self.diccionario_sig_palabra[sig_palabra] += 1
        else:
            self.diccionario_sig_palabra[sig_palabra] = 1
        
    def agrega_sig_patron(self, sig_patron):
        if sig_patron in self.diccionario_sig_patron.keys():
            self.diccionario_sig_patron[sig_patron] += 1
        else:
            self.diccionario_sig_patron[sig_patron] = 1

    def conteo_a_probabilidad(self):
        aux = 0
        for conteo in self.diccionario_sig_palabra:
            aux = aux + self.diccionario_sig_palabra.get(conteo)
        for conteo in self.diccionario_sig_palabra:
            self.diccionario_sig_palabra[conteo] = (self.diccionario_sig_palabra.get(conteo) /aux) * 100 
    
    def cierra_tabla(self):
        self.conteo_a_probabilidad()
        self.ordena_diccionario()

    def get_sig_palabra(self, probabilidad):
        aux = len(self.tupla_sig_palabras)//3
        if probabilidad == 'a' or probabilidad == 'A':
            aleatorio = random.randint(0, aux)
        elif probabilidad == 'b' or probabilidad == 'B':
            aleatorio =  len(self.tupla_sig_palabras) -1
        elif probabilidad == 'm' or probabilidad == 'M':
            aleatorio = random.randint(aux, aux*2)
        
        return self.tupla_sig_palabras[aleatorio][0]

    def ordena_diccionario(self):
        self.tupla_sig_palabras = sorted(self.diccionario_sig_palabra.items(), key=operator.itemgetter(1), reverse=True) 