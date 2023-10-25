import math

class Figura:
    def __init__(self):
        pass
    
    def area(self):
        pass
    
    def perim(self):
        pass
    


class Cuadrado(Figura):
        def __init__(self, lado):
            self.lado = lado
        
        def area(self):
            return  self.lado * self.lado
        
        def perim(self):
            return 4 * self.lado

class Circulo(Figura):
        def __init__(self, radio):
            self.radio = radio
            
        def area(self):
             return math.pi * self.radio * self.radio
         
        def perim(self):
            return 2 * math.pi * self.radio      