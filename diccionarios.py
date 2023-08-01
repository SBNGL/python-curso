#Diccionarios

persona = {
    'name' : 'Blair',
    'age' : 18,
    'boyfriend' : 'chuck',
    'list' : ['carro', 'iphone', 'computer'],
    'casado' : True
}
persona['hijos'] = 1

#print(persona.get('age'))
#print(persona.keys())
#print(persona.values())
#print(persona.items())
#persona.pop('age')
persona.update({'mascota' : True})
#print(persona)
#for k, v in persona.items():
 #   print(k, v)
#Tuplas
tupla = (123, 'Sebas', 17, 1.71)
#print(tupla.count('Sebas'))

#Set (Conjuntos)

a = {'s', 'g', 'l', 'c', 'c', 'p', 'g', 'v', 'a'}
b = set('sglccpgva')
#print(a)
#print(b)
#print(a - b)
#print(a | b)
#print(a & b)

s = {'carro', 'moto', 'bus'}
n = {'iphone', 'moto', 'computador'}
g = s.difference(n)
s.add('avión')
s.discard('bus')
print(s)