import math

class Figura:
    area = None
    perim = None
    
    def __init__(self):
        pass
    
    def Calculararea(self):
        pass
    
    def Calcularperim(self):
        pass
    


class Cuadrado(Figura):
    def __init__(self, lado):
        self.nombre = __class__.__name__
        self.lado = lado
        
    def Calculararea(self):
        self.area = self.lado * self.lado
        
    def Calcularperim(self):
        self.perim = 4 * self.lado
        
    def __str__(self):
        return f'{self.nombre}, lado:{self.lado}'

class Circulo(Figura):
    
    def __init__(self, radio):
        self.nombre = __class__.__name__
        self.radio = radio
              
    def Calculararea(self):
        self.area = math.pi * self.radio * self.radio
         
    def Calcularperim(self):
        self.perim = 2 * math.pi * self.radio     
        
    def __str__(self):
        return f'{self.nombre}, radio:{self.radio}'

def mostrarDatos(figura):
    figura.Calculararea()
    figura.Calcularperim()
    print(figura)        
    print('Area: ', figura.area())
    print('Perimetro: ', figura.perim())