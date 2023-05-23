# NÚMERO PERFEITO

x = int(input(''))
for i in range (x):

    number = int(input(''))
    acu = 0

    for i in range (1, number):
            if number % i == 0:
                    acu += i

    if acu == number:
        print(f'{number} eh perfeito')
    else:
        print(f'{number} nao eh perfeito')