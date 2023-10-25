from ejercicios import Circulo, Cuadrado

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
            print('Area: ', cuadrado.area)
            print('Perimetro: ', cuadrado.perim)
        elif opcion == "2":
            radio = float(input('Ingrese el radio del circulo: '))
            circulo = Circulo(radio)
            print('Area: ', circulo.area)
            print('Perimetro: ', circulo.perim)
        elif opcion == "3":
            break
        else:
            print('Opcion incorrecta')

main()    