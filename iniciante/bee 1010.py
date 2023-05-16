# CÁLCULO SIMPLES
peça1, num_peça1, valorUni_peça1 = input().split(' ')
peça2, num_peça2, valorUni_peça2 = input().split(' ')
print(f'VALOR A PAGAR: R$ {(int(num_peça1) * float(valorUni_peça1)) + (int(num_peça2) * float(valorUni_peça2)):.2f}')