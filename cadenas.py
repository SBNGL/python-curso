#Metodos para manipular cadenas str
'''
def get_string_metodos():
    i = 0
    for metodo in dir(str):
        if '__' not in metodo:
            i += 1
            print(i, metodo, sep=':')

get_string_metodos()            
'''

#Capitalize
'''''
text = 'sebas'
print(text.capitalize())
'''''

#casefold
'''''
text = 'Sebas'
print(text.casefold())
'''''

#center
'''''
text = 'Sebas'
print(text.center(60, '-'))
'''''

#count
'''''
text = 'sebastian'
print(text.count('a'))
'''''

#endswith
'''''
text = 'sebastian gomez lerma'
print(text.endswith('ma'))
'''''

#expandtabs
'''''
text = 'seb\tast\tian'
print(text.expandtabs(20))
'''''

#find and rfind
'''''
text = 'Sebastian Gomez Lerma'
posicion = text.find('Gomez')
print(posicion)
print(text[posicion:])
'''''

#format
'''''
text = '{nombre} es {cualidad}'
print(text.format(nombre = 'Sebastian', cualidad = 'Bonito'))

text = '{} es {}'
print(text.format('Sebastian', 'hermoso'))
'''''

#format_map
'''''
edades = { 'x': 18, 'y': 30 }
text = 'sebastian tiene: {x}, Ariana Grande tiene {y}'
print(text.format_map(edades))
'''''

#index
'''''
text = 'Sebastian Gomez'
print(text.index('G'))
'''''

#isdecimal
'''''
text = '123'
print(text.isdecimal())
'''''
#isdigit
'''''
text = '123'
print(text.isdigit())
'''''
#isnumeric
'''''
text = '123'
print(text.isnumeric())
'''''

#islower
"""""
text = 'sebas'
print(text.islower())
"""""
#isupper
'''''
text = 'SEBAS'
print(text.isupper())
'''''

#istitle
'''''
text = 'Megalodon El Gran Abismo'
print(text.istitle())
'''''

# lower, upper
'''
text = 'sebas'
print(text.lower())
print(text.upper())
'''

# join
'''
text = '_'
print(text.join(['Maria', 'Estela', 'Lerma']))
'''

#ljust, rjust
'''
text = 'cristina'
print(text.ljust(16, '+'))
print(text.rjust(16, '-'))
'''

#lstrip, rstrip
'''
text = 'camila cabello'
print(text.lstrip('camila'))
print(text.rstrip('cabello'))
'''

#translate, maketrans
'''
text = 'prueba ahora'
table = text.maketrans('a', 'A')
print(table)
print(text.translate(table))
'''

#partition
'''
text = 'G+G=GossipGirl'
print(text.partition('='))
'''

#removeprefix, removesuffix
'''
text = 'Netflix'
print(text.removeprefix('Net'))
print(text.removesuffix('flix'))
'''

#replace
'''
text = 'recuerda pedir tus brownie'
print(text.replace('brownie', 'brownies'))
'''

#split, rsplit
'''
text = 'Esto es una prueba para ver so sirve'
print(text.split(sep=' ', maxsplit= 2))
'''