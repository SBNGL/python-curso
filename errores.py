
while True:
    try:
        edad = int(input('¿Cual es tu edad?: '))
        div = 10/edad
        print(edad)
    except (ValueError, ZeroDivisionError) as err:
        print('lo ingresado es incorrecto, ', err)  
    else:
        print('Gracias')
        break    
    finally:
        print('Se acabó el programa..')
        
    