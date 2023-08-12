import random

num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
pares = []
impares = []

def agregarArreglos(num, n, aleatorio):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
        
    print(f'{n} x {aleatorio} = {num}')    


for n in num:
    aleatorio = random.randint(1, 100)
    agregarArreglos(n * aleatorio, n, aleatorio)

print('Lista de Pares: ', pares )
print('Lista de impares: ', impares)
             