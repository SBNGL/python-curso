def factorial(numero):
    if numero > 1:
        numero = numero * factorial(numero - 1)
    return numero

def contador_atras(numero):
    numero -= 1
    if(numero > 0):
        print(numero)
        contador_atras(numero)
    else:
        print('Fin')
    
    print(f'Liberacion: {numero}')
         
contador_atras(6)


#numero = int(input('Ingrese un número: '))


#print('El factorial es:' , factorial(numero))