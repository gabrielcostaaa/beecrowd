# O MAIOR
a, b, c = input().split()

maior_ab = (int(a) + int(b) + abs(int(a) - int(b))) / 2
maior = int((maior_ab + int(c) + abs(maior_ab - int(c))) / 2)

print(f"{maior} eh o maior")