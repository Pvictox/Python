#Desafio 96
'''
def area(base,altura):
    return base*altura

print(f'{area(float(input()), float(input()))}\n')
'''
#Desafio 97
'''
def escreva(msg):
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))

escreva('Pedro Victor de Abreu Fonseca')
'''
#Desafio 98
'''
def cont(inicio, fim, passo):
    for x in range(1,11):
        print(x, end=' ')
    print()
    for x in range(10,-1,-2):
        print(x, end=' ')
    print()
    if passo == 0:
        if inicio > fim:
            passo = -1
        else:
            passo = 1
    for x in range(inicio,fim-1,passo):
       print(x, end=' ') 
     
cont(5,3,0)
'''
#Desafio 99
'''
def maior(x):
    ref = x[0]
    for i in x:
        if i > ref:
            ref = i
    print(f'{ref}')

l = list()
while True:
    l.append(int(input()))
    if str(input('S/N')) == 'n':
        break
maior(l)
'''
#Desafio 100
'''
l = list()
from random import randint
def somaPar(l):
    soma = 0
    for x in l:
        if x%2==0:
            soma+=x
    return soma

def sorteia(l):
    for x in range(0,5):
        l.append(randint(1,100))
    soma = somaPar(l)
    print(f'A lista é {l} e a soma é {soma}')

sorteia(l)
'''