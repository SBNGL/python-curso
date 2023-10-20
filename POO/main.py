from poo import persona, animales
from Player import player
from persona import Persona, Usuario, Empleado
'''
Anim = animales() #Instancia de la clase (objeto)
Anim.getDatos()
'''
'''
perfil = persona('Arlex', 25, 234562)    
perfil.getDatos()  
'''
'''
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('Sebas'))
print(type([]))
print(type({}))
print(type(()))
'''
'''
print(player.agregar_datos2(2000))
print(player.agregar_datos(5000))
'''
'''
player1 = player('Sebastian', 18)
player2 = player('LA OFENDIDA', 17)
'''
#Acceso a los miembros de la clase
'''
pers1 = persona('Sebastian', 18, 123456)
pers2 = persona('Blair', 18, 5894613)

pers1.set_nombre = 'Chuck'
print(pers1.set_nombre)
print(pers2.set_nombre)
'''

personas = Persona('SHAKIRA', 17)
usuario = Usuario('KAROL G', 18)
empleado = Empleado('Sebas', 18, 20000000)
usuario.getDatos()
empleado.getDatos()
#personas.getDatos()