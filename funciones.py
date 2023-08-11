#Funciones basicas
def saludar(nombre):
    return(f'Hola, {nombre} desde la funcion 1')
    
def sumar(a, b):
    return a + b  

def multiplicar(a, b):
    return a * b  
    
saludo = saludar('Sebas')
print(saludo)


multiplicacion = multiplicar(23, 42)
print('El resultado es: ', multiplicacion)

#Funciones cob argumentos indefinidos
def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma += n
    
    return suma, kwargs
    
suma, datos = sumar(19, 63, 44, nombre = 'Sebastian', cosa = 'boligrafo' )
print('La suma es: ', suma)
print('Datos: ', datos)    