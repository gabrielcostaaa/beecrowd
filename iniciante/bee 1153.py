# FATORIAL SIMPLES

N = int(input(''))
W = 1
for i in range (N+1):
    if i == 0:
        nada=0
    else:
        W *= i
print(W)