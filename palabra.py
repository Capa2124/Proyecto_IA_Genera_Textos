import operator
import random

class Palabra:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.num_ocurrencia    = 0
        self.num_sig_palabra   = 0
        self.diccionario_sig_palabra = {}
        self.diccionario_sig_patron = {}
        self.tupla_sig_patron = ()
        self.tupla_sig_palabra = ()
    
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
        

    def elimina_sig_palabra(self, palabra_eliminar):
        aux = True
        if palabra_eliminar in self.diccionario_sig_palabra:
            del self.diccionario_sig_palabra[palabra_eliminar]
            self.conteo_a_probabilidad()
        else:
            aux = False
        return aux

    def conteo_a_probabilidad(self):
        aux = 0
        for conteo in self.diccionario_sig_palabra:
            aux = aux + self.diccionario_sig_palabra.get(conteo)
        for conteo in self.diccionario_sig_palabra:
            self.diccionario_sig_palabra[conteo] = (self.diccionario_sig_palabra.get(conteo) /aux) * 100 
        aux = 0
        for conteo in self.diccionario_sig_patron:
            aux = aux + self.diccionario_sig_patron.get(conteo)
        for conteo in self.diccionario_sig_patron:
            self.diccionario_sig_patron[conteo] = (self.diccionario_sig_patron.get(conteo) /aux) * 100 
    
    def cierra_tabla(self):
        self.conteo_a_probabilidad()
        self.ordena_diccionario()

    def get_sig_patron(self, probabilidad):
        aux = len(self.tupla_sig_patron)//3               #0  alta    1  media     2    baja   3
        if probabilidad == 'a' or probabilidad == 'A': #   (///////// | ////////// | //////////)
            aleatorio = random.randint(0, aux)
            #return self.tupla_sig_palabra[aleatorio][0]
        elif probabilidad == 'b' or probabilidad == 'B':
            aleatorio =  random.randint(aux*2-1, len(self.tupla_sig_patron) -1)
            #aleatorio = random.randint(len(self.tupla_sig_palabra) - 2, len(self.tupla_sig_palabra))
            #return self.tupla_sig_palabra[len(self.tupla_sig_palabra)][0]
        elif probabilidad == 'm' or probabilidad == 'M':
            aleatorio = random.randint(aux, aux*2)
            #return self.tupla_sig_palabra[len(self.tupla_sig_palabra)/2][0]
            #aleatorio = random.randint(len(self.tupla_sig_palabr)/2 - 1 , len(self.tupla_sig_palabra)/2+1)
        return self.tupla_sig_patron[aleatorio][0]

    def get_sig_palabra(self, probabilidad):
        aux = len(self.tupla_sig_palabra)//3
        if probabilidad == 'a' or probabilidad == 'A':
            aleatorio = random.randint(0, aux)
            #return self.tupla_sig_palabra[aleatorio][0]
        elif probabilidad == 'b' or probabilidad == 'B':
            aleatorio =  len(self.tupla_sig_palabra) -1
            #aleatorio = random.randint(len(self.tupla_sig_palabra) - 2, len(self.tupla_sig_palabra))
            #return self.tupla_sig_palabra[len(self.tupla_sig_palabra)][0]
        elif probabilidad == 'm' or probabilidad == 'M':
            aleatorio = random.randint(aux, aux*2)
            #return self.tupla_sig_palabra[len(self.tupla_sig_palabra)/2][0]
            #aleatorio = random.randint(len(self.tupla_sig_palabr)/2 - 1 , len(self.tupla_sig_palabra)/2+1)
        return self.tupla_sig_palabra[aleatorio][0]

#Para acceder a la clave se usa self.tupla_sig_palabra[1][0]
#Para acceder al valor se usa   self.tupla_sig_palabra[0][1]
    def ordena_diccionario(self):
        self.tupla_sig_palabra = sorted(self.diccionario_sig_palabra.items(), key=operator.itemgetter(1), reverse=True) 
        self.tupla_sig_patron  = sorted(self.diccionario_sig_patron.items(), key=operator.itemgetter(1), reverse=True) 
        
        