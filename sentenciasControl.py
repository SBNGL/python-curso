""""""""""
num = int(input('Ingrese un numero: '))


if num != 0:
    if num > 0:
        if num % 2 == 0:
            print(f'El número {num} par positivo')
        else:
            print(f'El número {num} impar positivo')
    else:
        if num % 2 == 0:
            print(f'El número {num} es par negativo')
        else:
            print(f'El número {num} es impar negativo')            
else:
    print(f'El numero {num} es neutro')        
"""""""""
"""""
vocal = input('Ingrese la letra: ')

if vocal == 'a':
    print(vocal, 'es una vocal')
elif vocal == 'e':
    print(vocal, 'es otra vocal')
elif vocal == 'i':
    print(vocal, 'es otra vocal')
elif vocal == 'o':
    print(vocal, 'es otra vocal')
elif vocal == 'u':
    print(vocal, 'es otra vocal')            
else:
    print('es otra letra')       
"""""

#while
"""""
num = int(input('Ingrese el número: '))
cont = 1
suma = 0
while cont <= num:
    suma += cont
    cont += 1

print(suma)
"""""

#Mostrar el número menor de n números ingresados
"""""
n = int(input('Cantidad de números: '))
menor = 0
i = 1
while(i <= n):
    numero = int(input('Número: '))
    if(i == 1):
        menor = numero
    elif numero < menor:
        menor = numero
    i += 1    

print(f'el número menor es: {menor}')                     
"""""
#For
palabras = ['Burbuja', 'Bombon', 'Bellota']
for p in palabras:
    print(p, len(p))
    
    
for s in range(6):
    print(s)    