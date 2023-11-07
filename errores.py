
while True:
    try:
        edad = int(input('¿Cual es tu edad?: '))
        div = 10/edad
        print(edad)
    except ValueError:
        print('Ingrese un numero entero')
    except ZeroDivisionError:
        print('No se puede dividir entre 0')       
    else:
        print('Gracias')
        break    
        
    