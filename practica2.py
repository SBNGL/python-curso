import random

num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
pares = []
impares = []

for n in num:
    aleatorio = random.randint(1, 100)
    result = n * aleatorio
    
    print(f'{n} x {aleatorio} = {result}')
    if result % 2 == 0:
        pares.append(result)
    else:
        impares.append(result)

print('Lista de Pares: ', pares )
print('Lista de impares: ', impares)
             