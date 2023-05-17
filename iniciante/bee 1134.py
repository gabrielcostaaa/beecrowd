#TIPO DE COMBUSTÍVEL
tipo_diesel = 0
tipo_gasolina = 0
tipo_alcool = 0

tipo = int(input(''))

while True:
    if tipo == 1:
        tipo_alcool += 1
        tipo = int(input(''))
    elif tipo == 2:
        tipo_gasolina += 1
        tipo = int(input(''))
    elif tipo == 3:
        tipo_diesel += 1
        tipo = int(input(''))
    elif 4 < tipo:
        tipo = int(input(''))
    else:
        break

print(f'MUITO OBRIGADO\nAlcool: {tipo_alcool}\nGasolina: {tipo_gasolina}\nDiesel: {tipo_diesel}')