# TIPOS DE TRIANGULOS
a, b, c = map(float,input().split())


if a >= b + c or b >= a + c or c >= b + a:
  print("NAO FORMA TRIANGULO")
else:
  if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b **2:
    print("TRIANGULO RETANGULO")
  elif a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > b**2 + a**2:
    print("TRIANGULO OBTUSANGULO")
  elif a**2 < b**2 + c**2 or b**2 < a**2 + c**2 or c**2 < b**2 + a**2:
    print("TRIANGULO ACUTANGULO")
  if a == b == c:
    print("TRIANGULO EQUILATERO")
  elif a == b or a == c or c == b:
    print("TRIANGULO ISOSCELES")