# SOMA DE IMPARES CONSECUTIVOS
x = int(input(''))
y = int(input(''))
soma_impares = 0


if x > y:
    x, y = y, x

for n in range (x+1, y):
    if n % 2 != 0:
        soma_impares += n
print(soma_impares)