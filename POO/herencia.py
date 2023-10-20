class PadreA:
    def __init__(self):
        print('Soy padre A')
        
    def a(self):
        print('Soy un metodo Padre A')
        
class PadreB:
    
    def __init__(self):
        print('Soy objeto PadreB')
        
    def b(self):
        print('Soy metodo padreB')
        
class HijoC(PadreA, PadreB):
    def c(self):
        print('Soy metodo HijoC')
        
#instanciacion
hijosc = HijoC()        
hijosc.a()
hijosc.b()
hijosc.c()
     
                          