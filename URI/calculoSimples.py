'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, 
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. 
Após, calcule e mostre o valor a ser pago.
'''
cod1, num1 = int(input()), int(input())
val1 = float(input())
cod2, num2 = int(input()), int(input())
val2 = float(input())
print(f'VALOR A PAGAR: R$ {(num1*val1)+(num2*val2):.2f}\n')