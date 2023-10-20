class animales:
    domesticos = 'perro', 'gato'
    mamiferos = 'ballena', 'canguro', 'koala'
    reptiles = 'serpiente'
    aves = 'paloma'
    
    def getDatos(self):
        print('domesticos: ', self.domesticos)
        print('mamiferos:', self.mamiferos)
        print('reptiles:', self.reptiles)
        print('aves:', self.aves)


class persona:
    __nombre = None
    __edad = None
    __numero = None
       
    def __init__(self, nom, ed, num):
        self.__nombre = nom
        self.__edad = ed
        self.__numero = num
    
    def getDatos(self):
        print('Nombre: ', self.nombre)
        print('Edad: ', self.edad)
        print('Numero: ', self.numero)
        
    def get_nombre(self):
        return self.__nombre    
    
    def get_edad(self):
        return self.__edad
    
    def get_numero(self):
        return self.__numero
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_nombre(self, edad):
        self.__edad = edad    
        
    def set_nombre(self, numero):
        self.__numero = numero    