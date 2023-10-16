#Definimos la clase

class player:
    #atributo de objeto de clase
    membresia = True
    
    def __init__(selft, nombre, edad):
        selft.nombre = nombre
        selft.edad = edad
        
    def ejecutar(self):
        print('RUN')
        return 'ok'   
    
    def datos(self):
        print(f'Mi nombre es {self.nombre}')
        
    def getMembresia(self):
        if player.membresia:
            print('Si')
        else:
            print('No')   
    
    #decorador

    @classmethod
    def agregar_datos(cls, score):
        return score     
    
    @staticmethod
    def agregar_datos2(score):
        return score       
                 