from ejercicios import Circulo, Cuadrado, mostrarDatos

def main():
    while True:
        menu = """"
        Menu de opciones
        """"""""""""""""""
        Calcule el area y perimetro de:
        1. Cuadrado
        2. Circulo
        3. Salir
        
        Ingrese la opcion:
        """
        
        opcion = input(menu)
        
        if opcion == "1":
            lado = float(input('Ingrese el lado del cuadrado: '))
            cuadrado = Cuadrado(lado)
            mostrarDatos(cuadrado)
        elif opcion == "2":
            radio = float(input('Ingrese el radio del circulo: '))
            circulo = Circulo(radio)
            mostrarDatos(circulo)
        elif opcion == "3":
            break
        else:
            print('Opcion incorrecta')

main()    