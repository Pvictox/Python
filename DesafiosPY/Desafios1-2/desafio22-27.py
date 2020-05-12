#Desafio 22
'''
nome = input() 
print(f'Maiusculo: {nome.upper()}\n')
print(f'Minusculo: {nome.lower()}\n')
x = nome.split()
y = ''.join(x)
print(f'Letras sem espaço: {len(y)}\n')
print(f'Letras do primeiro nome: {len(x[0])}\n')
'''
#Desafio 23
'''
num = int(input())
uni = num%10
dez = num%100
dez = dez//10
cent = num%1000
cent = cent // 100
mil = num // 1000
print(f'Unidade {uni}\n')
print(f'Dezena {dez}\n')
print(f'Cent {cent}\n')
print(f'Milhar {mil}')
'''
#Desafio 24
'''
cidade = input()
x = cidade[0:]
x = x.upper()
va = 'SANTO' in x
x = x.title()
print(f'{va}')
'''
#Desafio 25
'''
nome = input()
nome = nome.upper()
val = 'SILVA' in nome
nome = nome.title()
print(f'{val}')
'''
#Desafio 26
'''
frase = input()
print(f'Aparece {frase.count("a")} vezes')
print(f'Primeira vez: posição {frase.find("a")}')
print(f'Ultima vez: posição {frase.rfind("a")}')
'''
#Desafio 27
'''
nome = input()
y = nome.split()
print(f'Primeiro {y[0]}\nUltimo {y[len(y)-1]}')
'''
