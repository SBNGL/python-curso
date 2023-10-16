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
    def __init__(self, nom, ed, num):
        self.nombre = nom
        self.edad = ed
        self.numero = num
    
    def getDatos(self):
        print('Nombre: ', self.nombre)
        print('Edad: ', self.edad)
        print('Numero: ', self.numero)
        